import tkinter as tk
from tkinter import filedialog, Label, Button, Scale, HORIZONTAL, messagebox
from PIL import Image
import os

class ImageCompressorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("이미지 최적화 도구 made by dev.kiwon")
        self.master.geometry("500x400")  # 창 크기 설정

        # 폴더 선택 라벨
        self.path_label = Label(master, text="최적화할 이미지가 저장된 폴더를 선택해주세요")
        self.path_label.pack(pady=10)

        # 폴더 선택 버튼
        self.folder_btn = Button(master, text="폴더 선택", command=self.select_folder, cursor="hand2")
        self.folder_btn.pack(pady=(0,20))

        # 축소율 슬라이더
        self.scale_label = Label(master, text="가로/세로 사이즈 압축률 (10 ~ 100%):")
        self.scale_label.pack()
        self.scale_slider = Scale(master, from_=10, to=100, orient=HORIZONTAL)
        self.scale_slider.set(80)
        self.scale_slider.pack(pady=(5,40))

        # 품질 슬라이더
        self.quality_label = Label(master, text="품질 압축률 (10 ~ 100%):")
        self.quality_label.pack()
        self.quality_slider = Scale(master, from_=10, to=100, orient=HORIZONTAL)
        self.quality_slider.set(80)
        self.quality_slider.pack(pady=(5,20))

        # 압축 시작 버튼
        self.compress_btn = Button(master, text="압축 시작하기!", command=self.compress_images, state="disabled", cursor="hand2")
        self.compress_btn.pack(pady=(20, 10))

        # 상태 메시지 라벨
        self.status_label = Label(master, text="")
        self.status_label.pack(pady=10)

        # 변수 초기화
        self.input_directory = None
        self.output_directory = None

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.path_label.config(text=f"선택된 폴더: {folder_selected}")
            self.input_directory = folder_selected
            self.output_directory = os.path.join(os.path.dirname(self.input_directory), os.path.basename(self.input_directory) + '_compressed')
            self.compress_btn.config(state="normal")  # 폴더 선택 후 버튼 활성화
        else:
            messagebox.showwarning("Warning", "No folder selected!")

    # def compress_images(self):
    #     if not self.input_directory or not self.output_directory:
    #         messagebox.showwarning("Warning", "Please select a folder first!")
    #         return
    #     # 작업 시작 메시지 업데이트
    #     self.status_label.config(text="압축중입니다. 잠시만 기다려주세요", fg='white') 
    #     self.master.update()

    #     if not os.path.exists(self.output_directory):
    #         os.makedirs(self.output_directory)

    #     scale_factor = self.scale_slider.get() / 100.0
    #     quality = self.quality_slider.get()

    #     try:
    #         for filename in os.listdir(self.input_directory):
    #             if filename.lower().endswith('.jpg'):
    #                 file_path = os.path.join(self.input_directory, filename)
    #                 img = Image.open(file_path)
    #                 original_size = img.size
    #                 new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
    #                 img = img.resize(new_size, Image.Resampling.LANCZOS)
    #                 output_path = os.path.join(self.output_directory, filename)
    #                 img.save(output_path, 'JPEG', quality=quality)
    #         self.status_label.config(text="압축이 완료되었습니다!🎉", fg='yellow')
    #     except Exception as e:
    #         messagebox.showerror("Error", f"An error occurred: {str(e)}")
    #         self.status_label.config(text="An error occurred!")

    def compress_images(self):
        if not self.input_directory or not self.output_directory:
            messagebox.showwarning("Warning", "Please select a folder first!")
            return

        self.status_label.config(text="압축중입니다. 잠시만 기다려주세요", fg='white')
        self.master.update()

        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

        scale_factor = self.scale_slider.get() / 100.0
        quality = self.quality_slider.get()
        supported_extensions = ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.webp']

        try:
            for filename in os.listdir(self.input_directory):
                ext = os.path.splitext(filename)[1].lower()  # 파일 확장자 추출
                if ext in supported_extensions:
                    file_path = os.path.join(self.input_directory, filename)
                    img = Image.open(file_path)
                    original_size = img.size
                    new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
                    img = img.resize(new_size, Image.Resampling.LANCZOS)
                    output_path = os.path.join(self.output_directory, filename)
                    
                    # 확장자별 저장 옵션 설정
                    if ext in ['.jpeg', '.jpg']:
                        img.save(output_path, 'JPEG', quality=quality)
                    elif ext == '.png':
                        img.save(output_path, 'PNG', compression_level=9)
                    elif ext == '.gif':
                        img.save(output_path, 'GIF')
                    elif ext == '.bmp':
                        img.save(output_path, 'BMP')
                    elif ext == '.webp':
                        img.save(output_path, 'WEBP', quality=quality, lossless=False)

            self.status_label.config(text="압축이 완료되었습니다!🎉", fg='yellow')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_label.config(text="An error occurred!", fg='red')


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCompressorApp(root)
    root.mainloop()