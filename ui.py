import tkinter as tk
from tkinter import filedialog, messagebox
import json
import yaml
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=4)

def load_json_async(file_path):
  with open(file_path, 'r') as file:
    data = json.load(file)
  return data

def load_yaml_async(file_path):
  with open(file_path, 'r') as file:
    data = yaml.safe_load(file)
  return data

def load_xml_async(file_path):
  tree = ET.parse(file_path)
  root = tree.getroot()
  return root

def open_file():
  file_path = filedialog.askopenfilename()
  if file_path.endswith('.json'):
    future = executor.submit(load_json_async, file_path)
  elif file_path.ednswith('.yml') or file_path.endswith('.yaml'):
    future = executor.submit(load_yaml_async, file_path)
  elif file_path.endswith('.xml'):
    future = executor.submit(load_xml_async, file_path)
  else:
    messagebox.showerror("Error", "Unsupported file format")
    return

  def callback(fut):
    data = fut.result()
    messagebox.showinfo("File Content", str(data))

  future.add_done_callback(callback)

def main():
  root = tk.Tk()
  root.title("Simple UI")

  open_button = tk.Button(root, text="Open File", command=open_file)
  open_button.pack(pady=20)

  root.mainloop()

if __name__ == "__main__":
  main()
