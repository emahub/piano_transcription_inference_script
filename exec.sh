python3 -m venv venvdir
source venvdir/bin/activate

## setup
# python3 -m pip install librosa==0.9.2
# python3 -m pip install piano_transcription_inference
# python3 -m pip install setuptools
# python3 -m pip install torch
# brew install wget

python3 transcribe.py input.wav
