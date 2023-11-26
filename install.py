import launch
from importlib_metadata import version

def install():
    if launch.is_installed("tensorrt"):
        if not version("tensorrt") == "9.1.0.post12.dev4":
            launch.run(["python","-m","pip","uninstall","-y","tensorrt"], "removing old version of tensorrt")
        
    
    if not launch.is_installed("tensorrt"):
        print("TensorRT is not installed! Installing...")
        launch.run_pip("install --pre --extra-index-url https://pypi.nvidia.com tensorrt==9.1.0.post12.dev4 --no-cache-dir", "tensorrt", live=True)

    # Polygraphy	
    if not launch.is_installed("polygraphy"):
        print("Polygraphy is not installed! Installing...")
        launch.run_pip("install polygraphy --extra-index-url https://pypi.ngc.nvidia.com", "polygraphy", live=True)
    
    # ONNX GS
    if not launch.is_installed("onnx_graphsurgeon"):
        print("GS is not installed! Installing...")
        launch.run_pip("install protobuf==3.20.2", "protobuf", live=True)
        launch.run_pip('install onnx-graphsurgeon --extra-index-url https://pypi.ngc.nvidia.com', "onnx-graphsurgeon", live=True)
 
install()