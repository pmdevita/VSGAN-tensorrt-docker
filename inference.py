import sys

from pathlib import Path
sys.path.append(Path(__file__).parent)
from inference_config import inference_clip

video_path = "/xbox/dx2/dx_01.mkv"
clip = inference_clip(video_path)[:100]
clip.set_output()
