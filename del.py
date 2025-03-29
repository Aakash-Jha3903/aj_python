import os
import comtypes.client

def merge_ppts(folder_path, output_ppt):
    # Create a PowerPoint application object
    powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
    
    # Create a new presentation to store the merged slides
    merged_ppt = powerpoint.Presentations.Add()
    
    # Get a list of all PowerPoint files in the folder
    ppt_files = [f for f in os.listdir(folder_path) if f.endswith('.pptx')]
    
    for ppt_file in ppt_files:
        try:
            # Open each PowerPoint file in the folder
            presentation = powerpoint.Presentations.Open(os.path.join(folder_path, ppt_file))
            
            # Copy slides from the opened presentation to the merged presentation
            for i in range(1, presentation.Slides.Count + 1):
                merged_ppt.Slides.InsertFromFile(os.path.join(folder_path, ppt_file), i, 0)
            
            # Close the opened presentation
            presentation.Close()
        except Exception as e:
            print(f"Error processing '{ppt_file}': {e}")
    
    # Save the merged presentation
    merged_ppt.SaveAs(output_ppt)

    # Close PowerPoint application
    powerpoint.Quit()

folder_path = "C:\\Users\\Aakash Jha\\OneDrive\\Desktop\\del_PPT"
output_ppt = 'merged_ppt.pptx'
merge_ppts(folder_path, output_ppt)
