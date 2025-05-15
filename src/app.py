import PySimpleGUI as sg
import os
import cv2
from src.image_processor import ImageProcessor

class ImageFilterApp:
    def __init__(self):

        sg.theme('LightGrey1')
        
        self.original_image = None
        self.processed_image = None
        self.filter_history = []
        self.current_filters = []
        
        self.window = self.create_window()
        
    def create_window(self):

        control_column = [
            [sg.Text('Editor de Imagem', font=('Helvetica', 16, 'bold'), justification='center', expand_x=True)],
            [sg.Text('Selecione uma imagem:')],
            [sg.Input(key='-FILE-', size=(25,1)), 
             sg.FileBrowse('Procurar', file_types=(("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif"), ("Todos os Arquivos", "*.*")))],
            [sg.Button('Carregar Imagem', key='-LOAD-')],
            [sg.Text('Status:', key='-STATUS-', size=(30,1))],
            [sg.HorizontalSeparator()],
            
            [sg.Text('Filtros', font=('Helvetica', 14, 'bold'))],
            [sg.Checkbox('Escala de Cinza', key='-GRAY-')],
            [sg.Checkbox('Inverter Cores', key='-INVERT-')],
            [sg.Checkbox('Aumentar Contraste', key='-CONTRAST-')],
            [sg.Checkbox('Desfoque', key='-BLUR-')],
            [sg.Checkbox('Nitidez', key='-SHARPEN-')],
            [sg.Checkbox('Detecção de Bordas', key='-EDGES-')],
            
            [sg.HorizontalSeparator()],
            
            [sg.Text('Transformações', font=('Helvetica', 14, 'bold'))],
            [sg.Text('Rotação:')],
            [sg.Radio('90°', 'ROTATION', key='-ROTATE_90-', default=True),
             sg.Radio('180°', 'ROTATION', key='-ROTATE_180-'),
             sg.Radio('270°', 'ROTATION', key='-ROTATE_270-')],
            [sg.Button('Aplicar Rotação', key='-ROTATE-', size=(15, 1))],
            
            [sg.Text('Redimensionamento:')],
            [sg.Radio('50%', 'RESIZE', key='-RESIZE_50-', default=True),
             sg.Radio('200%', 'RESIZE', key='-RESIZE_200-')],
            [sg.Button('Aplicar Redimensionamento', key='-RESIZE-', size=(20, 1))],
            
            [sg.HorizontalSeparator()],
            
            [sg.Button('Aplicar Filtros', key='-APPLY-', size=(15, 1))],
            [sg.Button('Salvar Imagem', key='-SAVE-', size=(15, 1))],
        ]

        image_column = [
            [sg.Text('Imagem Original', font=('Helvetica', 12), justification='center', expand_x=True),
             sg.Text('Imagem Processada', font=('Helvetica', 12), justification='center', expand_x=True)],
            [sg.Image(key='-IMAGE_ORIGINAL-', size=(400, 400), background_color='lightgrey'),
             sg.Image(key='-IMAGE_PROCESSED-', size=(400, 400), background_color='lightgrey')]
        ]
     
        layout = [
            [sg.Column(control_column, vertical_alignment='top'),
             sg.VSeparator(),
             sg.Column(image_column, vertical_alignment='top')]
        ]
        
        return sg.Window('Visualizador e Editor de Imagens', 
                         layout, 
                         resizable=True, 
                         finalize=True)
    
    def load_image(self, file_path):

        img = ImageProcessor.load_image(file_path)
        if img is not None:
            self.original_image = img
            self.processed_image = img.copy()
            self.update_images()
            self.window['-STATUS-'].update(f'Imagem carregada: {os.path.basename(file_path)}', text_color='green')
            return True
        else:
            self.window['-STATUS-'].update('Falha ao carregar imagem', text_color='red')
            return False
    
    def update_images(self):

        if self.original_image is not None:
            self.window['-IMAGE_ORIGINAL-'].update(data=ImageProcessor.convert_to_bytes(self.original_image))
        if self.processed_image is not None:
            self.window['-IMAGE_PROCESSED-'].update(data=ImageProcessor.convert_to_bytes(self.processed_image))
    
    def apply_filters(self):

        if self.original_image is None:
            sg.popup_error('Nenhuma imagem carregada')
            return
            

        self.processed_image = self.original_image.copy()
        

        self.current_filters = []
        
        if self.window['-GRAY-'].get():
            self.processed_image = ImageProcessor.apply_grayscale(self.processed_image)
            self.current_filters.append('Escala de Cinza')
            
        if self.window['-INVERT-'].get():
            self.processed_image = ImageProcessor.apply_invert(self.processed_image)
            self.current_filters.append('Inversão de Cores')
            
        if self.window['-CONTRAST-'].get():
            self.processed_image = ImageProcessor.apply_contrast(self.processed_image)
            self.current_filters.append('Aumento de Contraste')
            
        if self.window['-BLUR-'].get():
            self.processed_image = ImageProcessor.apply_blur(self.processed_image)
            self.current_filters.append('Desfoque')
            
        if self.window['-SHARPEN-'].get():
            self.processed_image = ImageProcessor.apply_sharpen(self.processed_image)
            self.current_filters.append('Nitidez')
            
        if self.window['-EDGES-'].get():
            self.processed_image = ImageProcessor.apply_edge_detection(self.processed_image)
            self.current_filters.append('Detecção de Bordas')
        
        self.update_images()
        
        if self.current_filters:
            filters_text = ', '.join(self.current_filters)
            self.window['-STATUS-'].update(f'Filtros aplicados: {filters_text}', text_color='blue')
        else:
            self.window['-STATUS-'].update('Nenhum filtro selecionado', text_color='orange')

    
    def apply_transformation(self, transformation):

        if self.processed_image is None:
            sg.popup_error('Nenhuma imagem carregada')
            return
            
        if transformation == 'rotate':

            angle = 90  # Padrão
            if self.window['-ROTATE_90-'].get():
                angle = 90
            elif self.window['-ROTATE_180-'].get():
                angle = 180
            elif self.window['-ROTATE_270-'].get():
                angle = 270
                
            self.processed_image = ImageProcessor.apply_rotation(self.processed_image, angle)
            self.window['-STATUS-'].update(f'Rotação de {angle}° aplicada', text_color='blue')
            
        elif transformation == 'resize':
            scale = 0.5  # Padrão
            if self.window['-RESIZE_50-'].get():
                scale = 0.5
                scale_text = "50%"
            elif self.window['-RESIZE_200-'].get():
                scale = 2.0
                scale_text = "200%"
                
            self.processed_image = ImageProcessor.apply_resize(self.processed_image, scale)
            self.window['-STATUS-'].update(f'Redimensionamento para {scale_text} aplicado', text_color='blue')
            
        self.update_images()
    
    def save_image(self):
        if self.processed_image is None:
            sg.popup_error('Nenhuma imagem processada para salvar')
            return
            
        try:
            save_path = sg.popup_get_file('Salvar imagem como', save_as=True, no_window=True,
                                        file_types=(("PNG", "*.png"), ("JPEG", "*.jpg"), 
                                                   ("BMP", "*.bmp"), ("Todos os arquivos", "*.*")))
            if save_path:
                if not save_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                    save_path += '.png'
                    
                cv2.imwrite(save_path, self.processed_image)
                self.window['-STATUS-'].update(f'Imagem salva: {os.path.basename(save_path)}', text_color='green')
                sg.popup(f'Imagem salva com sucesso em:\n{save_path}')
        except Exception as e:
            sg.popup_error(f'Erro ao salvar a imagem: {str(e)}')
            self.window['-STATUS-'].update('Erro ao salvar imagem', text_color='red')
    
    def run(self):

        while True:
            event, values = self.window.read()
            
            if event == sg.WINDOW_CLOSED:
                break
                
            elif event == '-LOAD-':
                file_path = values['-FILE-']
                if file_path and os.path.exists(file_path):
                    self.load_image(file_path)
                else:
                    sg.popup_error('Arquivo não encontrado ou não selecionado.\nPor favor, selecione uma imagem válida.')
                    self.window['-STATUS-'].update('Nenhuma imagem carregada', text_color='red')
            
            elif event == '-APPLY-':
                self.apply_filters()
            
            elif event == '-ROTATE-':
                self.apply_transformation('rotate')
                
            elif event == '-RESIZE-':
                self.apply_transformation('resize')
            
            elif event == '-SAVE-':
                self.save_image()
        

        self.window.close()