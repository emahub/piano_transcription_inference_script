import sys
import os

from piano_transcription_inference import PianoTranscription, sample_rate, load_audio

def transcribe(audio_path, output_midi_path):
    # Load audio
    audio, _ = load_audio(audio_path, sr=sample_rate, mono=True)

    # Transcriptor
    # transcriptor = PianoTranscription(device='cuda', checkpoint_path=None)
    transcriptor = PianoTranscription(device='cpu', checkpoint_path=None)

    # Transcribe and write out to MIDI file
    transcriptor.transcribe(audio, output_midi_path)

# transcribe('input.wav', 'output.mid')


def convert_to_mid_filename(audio_path):
    base, _ = os.path.splitext(audio_path)
    return base + ".mid"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使い方: python script.py 入力ファイル.wav")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = convert_to_mid_filename(input_file)

    print("入力ファイル名:", input_file)
    print("出力ファイル名:", output_file)
    
    transcribe(input_file, output_file)
