Image ⇄ DNA Converters

This repository contains two graphical tools for converting between grayscale images (PNG format) and synthetic DNA sequences.


IMG2DNA: Image to DNA Converter

    Description: This tool allows users to convert a grayscale PNG image into a representation using DNA sequences. The pixel intensity values of the image are mapped to specific codons (DNA triplets). The generated DNA sequence can be viewed in the application's interface and saved to a .txt file.
    Usage:
        Launch the application.
        Click on "Open PNG Image" to load the image.
        The generated DNA sequence will be displayed in the text box.
        Click on "Save DNA Sequence" to save the sequence to a text file.
![img2dnaa](https://github.com/Ran2K-Creator/img2dna/assets/65309980/2f10ffd6-2d69-4745-8862-8c5a3f502e28)


DNA2IMG: DNA to Image Converter

    Description: This tool facilitates the process of converting a saved DNA sequence back into its original grayscale image representation. A DNA sequence, read from a .txt file, is translated into pixel intensity values to recreate the image. The regenerated image is displayed and can be saved in PNG format.
    Usage:
        Launch the application.
        Click on "Open DNA Sequence" to load the DNA sequence from a .txt file.
        The application processes the DNA sequence and generates a corresponding image, saving it as output.png.
        Click on "Save Image" to choose a different name or location to save the image.
![dna2img](https://github.com/Ran2K-Creator/img2dna/assets/65309980/57b4d3bc-4ccd-484d-8939-bb2a711d4311)


Dependencies

    tkinter: Used for the GUI interface.
    Pillow (PIL): For image processing tasks.
    numpy: For array manipulations during the conversion process.

Installation

pip3 install pillow numpy

Running the Tools

After installing the required dependencies, run the corresponding Python script for the desired converter.


Credits

Developed by Ran Malamud.
