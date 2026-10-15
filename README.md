# pdf-r

A simple PDF reader written in Python with tkinter and PyMuPDF.



## Features

- Open any PDF with a file picker
- Turn pages with the left and right arrow keys
- Remembers the last page you were on, separately for each book

## Requirements

- Python 3
- PyMuPDF

## Install

    python -m pip install pymupdf

## Run

    python pdfreader.py

Pick a PDF from the dialog. Cancelling closes the program.

## Controls

| Key   | Action        |
|-------|---------------|
| Right | Next page     |
| Left  | Previous page |

## How saving works

Each book gets its own save file named after the PDF (for example
`mybook.pdf.txt`), holding the page you were last on. Reopening that
book jumps straight back to it.

## About
might do a C rewrite in the future.

## Planned

- Page number display
- Zoom
- Fit the page to the window
