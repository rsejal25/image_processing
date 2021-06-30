import tkinter
import ctypes
import PIL
import os
import numpy	
import tkinter.messagebox
import cv2
import tkinter.ttk
import tkinter.filedialog
import PIL.ImageTk
import PIL.ImageFilter
import tkinter.colorchooser
class MainWindow(tkinter.Tk):
 image_file_list=[]
 def __init__(self):
  tkinter.Tk.__init__(self)
  self.title("IMagic")
  self.iconbitmap("icons/crop.ico")
  self.menuBar=tkinter.Menu(self,bg='#29A198')
  self.config(menu=self.menuBar,bg='#f2f2f2')
  #file menu
  image_file_list=[]
  self.fileMenu=tkinter.Menu(self.menuBar,tearoff=0,bg='#777b80')
  self.fileMenu.add_command(label="New")
  self.fileMenu.add_command(label="Open",command=self._openImage)
  self.fileMenu.add_command(label="Close")
  self.fileMenu.add_command(label="Save",command=self.imageSave)
  self.fileMenu.add_command(label="Save as")
  self.fileMenu.add_separator()
  self.fileMenu.add_command(label="Exit",command=self._exit)
  self.menuBar.add_cascade(label="File",menu=self.fileMenu)
  
  #edit menu
  #self.editMenu=tkinter.Menu(self.menuBar,tearoff=0)
  #self.editMenu.add_command(label="copy")
  #self.editMenu.add_command(label="cut")
  #self.editMenu.add_command(label="paste")
  #self.menuBar.add_cascade(label="Edit",menu=self.editMenu) 
  
  #view Menu
  self.viewMenu=tkinter.Menu(self.menuBar,tearoff=0,bg='#777b80')
  #self.viewMenu.add_command(label="Zoom in")
  #self.viewMenu.add_command(label="Zoom out")
  self.menuBar.add_cascade(label="View",menu=self.viewMenu)

  #view Menu-->magnification Menu
  self.magnificationMenu=tkinter.Menu(self.menuBar,tearoff=0,bg='#777b80')
  self.magnificationMenu.add_command(label="label=50%",command=self.magnify_image_by_50_)
  self.magnificationMenu.add_command(label="label=150%",command=self.magnify_image_by_150_)
  self.magnificationMenu.add_command(label="label=250%",command=self.magnify_image_by_250_)
  self.viewMenu.add_cascade(label="Magification",menu=self.magnificationMenu)
  
  #transform Menu
  self.transformMenu=tkinter.Menu(self.menuBar,tearoff=0,bg='#777b80')
  self.transformMenu.add_command(label="crop",command=self.crop_click)
  self.transformMenu.add_command(label="Rotate 90\u00B0 left",command=self.rotate_90_left)
  self.transformMenu.add_command(label="Rotate 90\u00B0 right",command=self.rotate_90_right)
  self.transformMenu.add_command(label="Rotate 180\u00B0",command=self.rotate_180_image)
  self.transformMenu.add_command(label="Flip Horizontal",command=self.flip_horizontal)
  self.transformMenu.add_command(label="Flip vertical",command=self.flip_vertical)
  self.menuBar.add_cascade(label="Transform",menu=self.transformMenu)


  #filter Menu
  self.filterMenu=tkinter.Menu(self.menuBar,tearoff=0,bg='#777b80')
  #self.filterMenu.add_command(label="Mean")
  self.filterMenu.add_command(label="Median",command=self.median_filter)
  #self.filterMenu.add_command(label="Fourier transform")
  self.filterMenu.add_command(label="Gaussian smoothing",command=self.gaussian_filter)
  #self.filterMenu.add_command(label="Unsharp")
  #self.filterMenu.add_command(label="Laplacian")
  self.menuBar.add_cascade(label="Filter",menu=self.filterMenu)


  self.toolBar=tkinter.Frame(self,relief=tkinter.RAISED,bd=1,bg='#29A198')
  self.toolBar.pack(side=tkinter.TOP,fill=tkinter.X)
  
  

  #ToolBar buttons
  #self.imagePick=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/cursor.png")) 
  #self.toolBarPickButton=tkinter.Button(self.toolBar,image=self.imagePick)
  #self.toolBarPickButton.pack(side=tkinter.LEFT,padx=3,pady=3) 
  
  self.imageNew=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/gallery.png"))
  self.toolBarNewButton=tkinter.Button(self.toolBar,image=self.imageNew,command=self.new_image)
  self.toolBarNewButton.pack(side=tkinter.LEFT,padx=3,pady=3)
 
  self.imageOpen=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/folder.png"))
  self.toolBarOpenButton=tkinter.Button(self.toolBar,image=self.imageOpen,command=self._openImage)
  self.toolBarOpenButton.pack(side=tkinter.LEFT,padx=3,pady=3)
  
  self.imageSave1=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/download.png"))
  self.toolBarSaveButton=tkinter.Button(self.toolBar,image=self.imageSave1,command=self.imageSave)
  self.toolBarSaveButton.pack(side=tkinter.LEFT,padx=3,pady=3)
 
  self.imageBrightness=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/brightness.png"))
  self.toolBarBrightnessButton=tkinter.Button(self.toolBar,image=self.imageBrightness,command=self.brightness_click)
  self.toolBarBrightnessButton.pack(side=tkinter.LEFT,padx=3,pady=3)
  
  self.imageContrast=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/contrast.png"))
  self.toolBarContrastButton=tkinter.Button(self.toolBar,image=self.imageContrast,command=self.contrast_click)
  self.toolBarContrastButton.pack(side=tkinter.LEFT,padx=3,pady=3)
  
  self.imageCrop=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/crop-tool.png"))
  self.toolBarCropButton=tkinter.Button(self.toolBar,image=self.imageCrop,command=self.crop_click)
  self.toolBarCropButton.pack(side=tkinter.LEFT,padx=3,pady=3)

  self.imageFlip=PIL.ImageTk.	PhotoImage(PIL.Image.open("icons/flip.png"))
  self.toolBarFlipButton=tkinter.Button(self.toolBar,image=self.imageFlip,command=self.flip_horizontal)
  self.toolBarFlipButton.pack(side=tkinter.LEFT,padx=3,pady=3)


  self.imageFlip1=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/flip (1).png"))
  self.toolBarFlip1Button=tkinter.Button(self.toolBar,image=self.imageFlip1,command=self.flip_vertical)
  self.toolBarFlip1Button.pack(side=tkinter.LEFT,padx=3,pady=3)



 
  self.imageGrayScale=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/greyscale.png"))
  self.toolBarGrayScaleButton=tkinter.Button(self.toolBar,image=self.imageGrayScale,command=self.grayScale_handler)
  self.toolBarGrayScaleButton.pack(side=tkinter.LEFT,padx=3,pady=3)

  self.imageOverlay=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/layers.png"))
  self.toolBarOverlayButton=tkinter.Button(self.toolBar,image=self.imageOverlay,command=self.overlay_handler)
  self.toolBarOverlayButton.pack(side=tkinter.LEFT,padx=3,pady=3)


  self.imageText=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/font.png"))
  self.toolBarTextButton=tkinter.Button(self.toolBar,image=self.imageText,command=self.text_on_image)
  self.toolBarTextButton.pack(side=tkinter.LEFT,padx=3,pady=3)



  self.imageUndo=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/undo.png"))
  self.toolBarUndoButton=tkinter.Button(self.toolBar,image=self.imageUndo,command=self.image_undo)
  self.toolBarUndoButton.pack(side=tkinter.LEFT,padx=3,pady=3)


  self.imagePdf=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/document.png"))
  self.toolBarPdfButton=tkinter.Button(self.toolBar,image=self.imagePdf,command=self.image_to_pdf)
  self.toolBarPdfButton.pack(side=tkinter.LEFT,padx=3,pady=3)


  self.imageExit=PIL.ImageTk.PhotoImage(PIL.Image.open("icons/exit.png"))
  self.toolBarExitButton=tkinter.Button(self.toolBar,image=self.imageExit,command=self._exit)
  self.toolBarExitButton.pack(side=tkinter.LEFT,padx=3,pady=3)

  self.imageContainerFrame=tkinter.Frame(self,bd=1)
  self.imageContainerFrame.pack(side=tkinter.LEFT,fill=tkinter.BOTH,expand=True)
  self.imageCanvas=tkinter.Canvas(self.imageContainerFrame)
  self.imageCanvas.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
  self.imageFileName=None
  self.currentImage=None
  

 def contrast_click(self):
  newin=tkinter.Toplevel(self,bg='#29A198')
  newin.title="Contrast"  
  newin.iconbitmap("icons/crop.ico")

  newin.geometry("250x200")
  newin.resizable(0,0)
  contrastFactor=tkinter.IntVar()
  contrast_label=tkinter.Label(newin,text='set Contrast',font=('Arial',25),bg='#29A198')
  contrast_label.grid(row=0,column=0,pady=5)
  scaler_contrast=tkinter.Scale(newin,from_=-255,to=255,length=200,orient='horizontal',variable=contrastFactor,command=self.contrast_handler,bg='#29A198')
  scaler_contrast.grid(row=1,column=0,padx=5,pady=10)
 
 def contrast_handler(self,contrastFactor):
  imageData=cv2.imread(self.imageFileName)
  contrast=int(contrastFactor)
  f=(259*(contrast+255))/(255*(259-contrast))
  for r in range(imageData.shape[0]):
   for c in range(imageData.shape[1]):
    rgb=imageData[r][c]
    blue=rgb[0]
    green=rgb[1]
    red=rgb[2]
    newRed=(f*(red-128))+128
    newGreen=(f*(green-128))+128
    newBlue=(f*(blue-128))+128
    if newRed>255: newRed=255
    if newRed<0: newRed=0
    if newGreen>255: newGreen=255
    if newGreen<0: newGreen=0
    if newBlue>255: newBlue=255
    if newBlue<0: newBlue=0
    imageData[r][c]=(newBlue,newGreen,newRed)
  cv2.imwrite("tmpFile_contrast.jpg",imageData)
  self.imageFileName=os.path.abspath("tmpFile_contrast.jpg")
  MainWindow.image_file_list.append(self.imageFileName)  

  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")
      

 def brightness_click(self):
  newin=tkinter.Toplevel(self,bg='#29A198')
  newin.title="Brightness"  
  newin.geometry("250x200")
  newin.iconbitmap("icons/crop.ico")

  newin.resizable(0,0)
  brightnessFactor=tkinter.IntVar()
  brightness_label=tkinter.Label(newin,font=('Arial',25),text='set Brightness',bg='#29A198')
  brightness_label.grid(row=0,column=0,padx=10,pady=5)
  scaler_brightness=tkinter.Scale(newin,from_=-255,to=255,length=200,orient='horizontal',variable=brightnessFactor,command=self.brightness_handler,bg='#29A198')
  scaler_brightness.grid(row=1,column=0,padx=5,pady=10)

 def brightness_handler(self,brightnessFactor):
  imageData=cv2.imread(self.imageFileName)
  brightness=int(brightnessFactor) 
  for r in range(imageData.shape[0]):
   for c in range(imageData.shape[1]):
    rgb=imageData[r][c]
    blue=rgb[0]
    green=rgb[1]
    red=rgb[2]
    red+=brightness
    green+=brightness
    blue+=brightness

    if red>255: red=255
    if red<0: red=0
    if green>255: green=255
    if green<0: green=0
    if blue>255: blue=255
    if blue<0: blue=0
    imageData[r][c]=(blue,green,red)
  cv2.imwrite("tmpFile_brightness.jpg",imageData)
  self.imageFileName=os.path.abspath("tmpFile_brightness.jpg")
  MainWindow.image_file_list.append(self.imageFileName)  

  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")
 

 def crop_handler(self,p,q,s,t):
  imageData=cv2.imread(self.imageFileName)
  print(p,q,s,t)
  cropFrom=(p,q)
  print(imageData)
  cropSize=(s,t)
  c1=cropFrom[0]
  r1=cropFrom[1]
  c2=cropSize[0]-1
  r2=cropSize[1]-1
  print(imageData.shape)
  if r2>=imageData.shape[0]: r2=imageData.shape[0]-1
  if c2>=imageData.shape[1]: c2=imageData.shape[1]-1
  print("Actual size",imageData.shape)
  print(cropSize)
  cropSize=(c2-c1+1,r2-r1+1)
  print(cropSize)
  r=r1
  while r<=r2:
   imageData[r][c1]=(0,0,255)
   imageData[r][c2]=(0,0,255)
   r+=1
  c=c1
  while c<=c2:
   imageData[r1][c]=(0,0,255)
   imageData[r2][c]=(0,0,255)
   c+=1

  newImage=numpy.zeros((cropSize[1],cropSize[0],3))
  rr=0
  r=r1
  while r<=r2:
   cc=0
   c=c1
   while c<=c2:
    newImage[rr][cc]=imageData[r][c]
    cc+=1
    c+=1
   rr+=1
   r+=1
  cv2.imwrite("tmpFile_crop.jpg",newImage)
  self.imageFileName=os.path.abspath("tmpFile_crop.jpg")
  MainWindow.image_file_list.append(self.imageFileName)  
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")


 def image_to_pdf(self):
  #newin=tkinter.Toplevel(self)
  #newin.geometry("500x200")
  #firstLabelFrame=tkinter.LabelFrame(newin)
  #firstLabelFrame.grid(row=0,column=0,padx=20,pady=20)
  #pdf_location=tkinter.StringVar()
  #self.text_label=tkinter.Label(firstLabelFrame,text="Location of pdf with name")
  #self.text_label.grid(row=0,column=0,padx=5,pady=10)

  #text_entry=tkinter.ttk.Entry(firstLabelFrame,width=30,textvariable=pdf_location)
  #text_entry.grid(row=0,column=1,padx=5,pady=10)
  #ok_button=tkinter.Button(firstLabelFrame,text="OK",command=lambda: self.image_to_pdf_handler(self.imageFileName,pdf_location.get()))
  #ok_button.grid(row=1,column=0,padx=30,pady=10)
  files=[('All Files','*.*'),('jpeg files','*.jpg'),('png files','*.png'),('pdf files','*.pdf')]
  a=tkinter.filedialog.asksaveasfile(filetypes=files,defaultextension=files)
  image1=PIL.Image.open(self.imageFileName)
  im1=image1.convert('RGB')
  print(a.name)
  im1.save(a.name)  
  tkinter.messagebox.showinfo("showinfo","Sucessfully converted to pdf")

  #image1=PIL.Image.open(self.imageFile)
  #im1=image1.convert('RGB')
  #im1.save('c:/')  


 def image_to_pdf_handler(self,imagePath,pdfLocation):
  image1=PIL.Image.open(imagePath)
  im1=image1.convert('RGB')
  print(pdfLocation)
  im1.save(pdfLocation)  
  tkinter.messagebox.showinfo("showinfo","Sucessfully converted to pdf")
  



 def overlay_handler(self):
  newin=tkinter.Toplevel(self,bg='#29A198')
  newin.geometry("400x200")
  newin.iconbitmap("icons/crop.ico")
  firstLabelFrame=tkinter.LabelFrame(newin,bg='#777b80')
  firstLabelFrame.grid(row=0,column=0,padx=30,pady=10)
  self.choosen=''
  chooseFileButton=tkinter.Button(firstLabelFrame,text="Choose Files",command=self.choose_image_)
  chooseFileButton.grid(row=0,column=0,padx=40,pady=10)
  position_x_label=tkinter.Label(firstLabelFrame,text="Position-X",bg='#777b80')
  position_x_label.grid(row=1,column=0,padx=10,pady=10)
  position_x=tkinter.IntVar()
  position_y=tkinter.IntVar()
  entryOfX=tkinter.ttk.Entry(firstLabelFrame,width=20,textvariable=position_x)
  entryOfX.grid(row=1,column=1,padx=10,pady=10)
  positionOfYLabel=tkinter.Label(firstLabelFrame,text="Position-Y",bg='#777b80')
  positionOfYLabel.grid(row=2,column=0,padx=10,pady=10)
  entryOfY=tkinter.ttk.Entry(firstLabelFrame,width=20,textvariable=position_y)
  entryOfY.grid(row=2,column=1,padx=10,pady=10)
  ok_button=tkinter.Button(firstLabelFrame,text="OK",command=lambda: self.overlay_ok_handler(position_x.get(),position_y.get(),self.choosen))
  ok_button.grid(row=4,column=0,padx=30,pady=10)


 def text_on_image(self):
  newin=tkinter.Toplevel(self,bg='#29A198')
  newin.geometry("500x300")
  newin.iconbitmap("icons/crop.ico")
  firstLabelFrame=tkinter.LabelFrame(newin,bg='#777b80')
  firstLabelFrame.grid(row=0,column=0,padx=30,pady=30)
  self.choosen=''
  textOnImage=tkinter.StringVar()
  self.text_label=tkinter.Label(firstLabelFrame,text="Write Text",bg='#777b80')
  self.text_label.grid(row=0,column=0,padx=5,pady=10)

  text_entry=tkinter.ttk.Entry(firstLabelFrame,width=30,textvariable=textOnImage)
  text_entry.grid(row=0,column=1,padx=5,pady=10)
  self.color_code=''
  colorButton=tkinter.Button(firstLabelFrame,text="Choose Color",command=self.choose_color)
  colorButton.grid(row=1,column=0,padx=5,pady=10)

  self.fontSizeLabel=tkinter.Label(firstLabelFrame,text="Font Size",bg='#777b80')
  self.fontSizeLabel.grid(row=1,column=1,padx=2,pady=10)
  self.fontSize=tkinter.IntVar()
  #self.fontLimit=tkinter.IntVar()
  self.fontLimitSpinBox=tkinter.ttk.Spinbox(firstLabelFrame,from_=1,to=50,textvariable=self.fontSize,state='readonly')
  self.fontLimitSpinBox.grid(row=1,column=2)
  self.fontSize.set(1)

  position_x_label=tkinter.Label(firstLabelFrame,text="Position-X",bg='#777b80')
  position_x_label.grid(row=2,column=0,padx=10,pady=10)
  position_x=tkinter.IntVar()
  position_y=tkinter.IntVar()
  entryOfX=tkinter.ttk.Entry(firstLabelFrame,width=20,textvariable=position_x)
  entryOfX.grid(row=2,column=1,padx=10,pady=10)
  positionOfYLabel=tkinter.Label(firstLabelFrame,text="Position-Y",bg='#777b80')
  positionOfYLabel.grid(row=3,column=0,padx=10,pady=10)
  entryOfY=tkinter.ttk.Entry(firstLabelFrame,width=20,textvariable=position_y)
  entryOfY.grid(row=3,column=1,padx=10,pady=10)
  
  ok_button=tkinter.Button(firstLabelFrame,text="OK",command=lambda: self.text_on_image_handler(position_x.get(),position_y.get(),self.color_code,textOnImage.get(),self.fontSize.get()))
  ok_button.grid(row=4,column=0,padx=30,pady=10)

 def choose_color(self): 
  # variable to store hexadecimal code of color
  self.color_code = tkinter.colorchooser.askcolor(title ="Choose color")
  print(self.color_code)
  #print(color_code)

 def text_on_image_handler(self,x,y,color,text,fontSize):
  thickness=2
  org=(x,y)
  color1=color[0]
  color2=(color1[2],color1[1],color1[0])
  print(type(color2))
  imageData=cv2.imread(self.imageFileName)
  font=cv2.FONT_HERSHEY_SIMPLEX
  image=cv2.putText(imageData,text,org,font,fontSize,color2,thickness, cv2.LINE_AA)
  cv2.imwrite("tmpFile_text_on_image.jpg",image)
  self.imageFileName=os.path.abspath("tmpFile_text_on_image.jpg")
  MainWindow.image_file_list.append(self.imageFileName)  
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")



 def overlay_ok_handler(self,x,y,file_choosen):
  Image1 = PIL.Image.open(self.imageFileName)
  
# make a copy the image so that 
# the original image does not get affected
  Image1copy = Image1.copy()
  Image2 = PIL.Image.open(file_choosen)
  Image2copy = Image2.copy()
  
# paste image giving dimensions
  Image1copy.paste(Image2copy, (70, 70))
  
# save the image 
  Image1copy.save('tmpFile_overlay.jpg')
  self.imageFileName=os.path.abspath("tmpFile_overlay.jpg")
  MainWindow.image_file_list.append(self.imageFileName)  
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")



 def choose_image_(self):
  self.choosen=tkinter.filedialog.askopenfilename(initialdir="/",title="Select Image File",filetype=(("jpeg file","*.jpg"),("png file","*.png")))
 



 def crop_click(self):
  newin=tkinter.Toplevel(self,bg='#29A198')
  newin.geometry("300x300")
  newin.iconbitmap("icons/crop.ico")
  firstLabelFrame=tkinter.LabelFrame(newin,bg='#777b80')
  firstLabelFrame.grid(row=0,column=0,padx=30,pady=30)
  positionOfXLabel=tkinter.Label(firstLabelFrame,text="Position-X",bg='#777b80')
  positionOfXLabel.grid(row=0,column=0,padx=10,pady=10)
  positionOfX=tkinter.IntVar()
  positionOfY=tkinter.IntVar()
  entryOfX=tkinter.ttk.Entry(firstLabelFrame,width=20,textvariable=positionOfX)
  entryOfX.grid(row=0,column=1,padx=10,pady=10)
  positionOfYLabel=tkinter.Label(firstLabelFrame,text="Position-Y",bg='#777b80')
  positionOfYLabel.grid(row=1,column=0,padx=10,pady=10)
  entryOfY=tkinter.ttk.Entry(firstLabelFrame,width=20,textvariable=positionOfY)
  entryOfY.grid(row=1,column=1,padx=10,pady=10)
  width_value=tkinter.IntVar()
  height_value=tkinter.IntVar()
  imageWidth=tkinter.Label(firstLabelFrame,text="Width",bg='#777b80')
  imageWidth.grid(row=2,column=0,padx=10,pady=10)
  width_entry=tkinter.ttk.Entry(firstLabelFrame,textvariable=width_value)
  width_entry.grid(row=2,column=1,padx=10,pady=10)
  imageHeight=tkinter.Label(firstLabelFrame,text="Height",bg='#777b80')
  imageHeight.grid(row=3,column=0,padx=10,pady=10)
  height_entry=tkinter.ttk.Entry(firstLabelFrame,width=20,textvariable=height_value)
  height_entry.grid(row=3,column=1,padx=10,pady=10)
  ok_button=tkinter.Button(firstLabelFrame,text="OK",command=lambda: self.crop_handler(positionOfX.get(),positionOfY.get(),width_value.get(),height_value.get()))
  ok_button.grid(row=4,column=0,padx=30,pady=10)
  


 def flip_vertical(self):
  imageData=cv2.imread(self.imageFileName)
  img2=numpy.zeros((imageData.shape[0],imageData.shape[1],3))
  for i in range(imageData.shape[0]):
    img2[i,:]=imageData[imageData.shape[0]-i-1,:]
  cv2.imwrite("tmpFile_flip_vertical.jpg",img2)  
  self.imageFileName=os.path.abspath("tmpFile_flip_vertical.jpg")
  MainWindow.image_file_list.append(self.imageFileName)  
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")




 def rotate_90_right(self):
  imageData=cv2.imread(self.imageFileName)
  empty_img=cv2.rotate(imageData,cv2.ROTATE_90_COUNTERCLOCKWISE)
  cv2.imwrite("tmpFile_90_right.jpg",empty_img)
  self.imageFileName=os.path.abspath("tmpFile_90_right.jpg")
  MainWindow.image_file_list.append(self.imageFileName)  
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")



 def rotate_90_left(self):
  img=cv2.imread(self.imageFileName)
  img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

  cv2.imwrite("tmpFile_rotate_90_left.jpg",img_rotate_90_clockwise)
  self.imageFileName=os.path.abspath("tmpFile_rotate_90_left.jpg")
  MainWindow.image_file_list.append(self.imageFileName)  
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")





 def rotate_180_image(self):
  imageData=cv2.imread(self.imageFileName)
  empty_img = numpy.zeros((imageData.shape[0],imageData.shape[1],3))
  h=imageData.shape[0]
  w=imageData.shape[1]

  for i in range(h):
    for j in range(w):
        empty_img[i,j] = imageData[h-i-1,w-j-1]
        empty_img = empty_img[0:h,0:w]
  cv2.imwrite("tmpFile_rotate_1_8_0.jpg",empty_img)
  self.imageFileName=os.path.abspath("tmpFile_rotate_1_8_0.jpg")
  #print(filePath)
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  MainWindow.image_file_list.append(self.imageFileName)
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")

 def grayScale_handler(self):
  imageData=cv2.imread(self.imageFileName)
  for r in range(imageData.shape[0]):
   for c in range(imageData.shape[1]):
    rgb=imageData[r][c]
    red=int(rgb[0])*0.11
    green=int(rgb[1])*0.59
    blue=int(rgb[2])*0.3
    total=red+blue+green
    imageData[r][c]=(total,total,total)
  cv2.imwrite("tmpFile_gray_scale.jpg",imageData) 
  self.imageFileName=os.path.abspath("tmpFile_gray_scale.jpg")
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  MainWindow.image_file_list.append(self.imageFileName)
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")


 def magnify_image_by_50_(self):
  img = cv2.imread(self.imageFileName)  
  
  #print('Original Dimensions : ', img.shape)  
  
  scale = 50  # percent of original size   
  width = int(img.shape[1] * scale / 100)  
  height = int(img.shape[0] * scale / 100)  
  dim = (width, height)  
# resize image  
  resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)  
  
#print('Resized Dimensions : ', resized.shape)  
  cv2.imwrite("tmpFile_maginfy_by_50_.jpg",resized)  
  self.imageFileName=os.path.abspath("tmpFile_maginfy_by_50_.jpg")
  MainWindow.image_file_list.append(self.imageFileName)
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")


 def magnify_image_by_150_(self):
  img = cv2.imread(self.imageFileName)  
  
  #print('Original Dimensions : ', img.shape)  
  
  scale = 150  # percent of original size   
  width = int(img.shape[1] * scale / 100)  
  height = int(img.shape[0] * scale / 100)  
  dim = (width, height)  
# resize image  
  resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)  
  
#print('Resized Dimensions : ', resized.shape)  
  cv2.imwrite("tmpFile_magnify_150_.jpg",resized)  
  self.imageFileName=os.path.abspath("tmpFile_magnify_150_.jpg")
  MainWindow.image_file_list.append(self.imageFileName)  
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")


 def magnify_image_by_250_(self):
  img = cv2.imread(self.imageFileName)  
  
  #print('Original Dimensions : ', img.shape)  
  
  scale = 250  # percent of original size   
  width = int(img.shape[1] * scale / 100)  
  height = int(img.shape[0] * scale / 100)  
  dim = (width, height)  
# resize image  
  resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)  
  
#print('Resized Dimensions : ', resized.shape)  
  cv2.imwrite("tmpFile_magnify_250_.jpg",resized)  
  self.imageFileName=os.path.abspath("tmpFile_magnify_250_.jpg")

  MainWindow.image_file_list.append(self.imageFileName)  

  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")




 def image_undo(self): 
  print(self.imageFileName)
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")

 def flip_horizontal(self):
  imageData=cv2.imread(self.imageFileName)
  flipped = cv2.flip(imageData,1)
  cv2.imwrite("tmpFile_flip_horizontal.jpg",flipped)
  self.imageFileName=os.path.abspath("tmpFile_flip_horizontal.jpg")
  MainWindow.image_file_list.append(self.imageFileName)  
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")
  
 def median_filter(self):
  image=PIL.Image.open(self.imageFileName)
  image2=image.filter(PIL.ImageFilter.MedianFilter(size=3))
  #cv2.imwrite("tmpFile.jpg",image2)
  self.currentImage=PIL.ImageTk.PhotoImage(image2)
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")

 def gaussian_filter(self):
  image=PIL.Image.open(self.imageFileName)
  image=image.filter(PIL.ImageFilter.GaussianBlur)
  self.currentImage=PIL.ImageTk.PhotoImage(image)
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")

 def _exit(self):
  self.quit()
  self.destroy()
  exit()
 def new_image(self):
  self.imageFileName=self.originalImageFileName
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.originalImageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")

 def image_undo(self):
  if len(MainWindow.image_file_list)>0:
   self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(MainWindow.image_file_list.pop()))
   self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")
    
   
 def _openImage(self):
  imgfn=tkinter.filedialog.askopenfilename(initialdir="/",title="Select Image File",filetype=(("jpeg file","*.jpg"),("png file","*.png")))
  self.imageFileName=imgfn
  self.originalImageFileName=self.imageFileName
  self.currentImage=PIL.ImageTk.PhotoImage(PIL.Image.open(self.imageFileName))
  self.imageCanvas.create_image(10,10,image=self.currentImage,anchor="nw")

 def imageSave(self):
  image=PIL.Image.open(self.imageFileName)
  files=[('All Files','*.*'),('jpeg files','*.jpg'),('png files','*.png')]
  a=tkinter.filedialog.asksaveasfile(filetypes=files,defaultextension=files)
  image.save(a)
myWindow=MainWindow()
myWindow.mainloop()                                     