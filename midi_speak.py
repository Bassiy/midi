import mido
from mido import MidiFile, MidiTrack, Message
import time

# 使用するMIDIファイルを指定
midi_file = 'yusha_level1.mid'
#midi_file = 'C:/Users/yu4to/OneDrive - nkz.ac.jp/ドキュメント/challenge/program/learn/midi/yusha_level1.mid'
mid = MidiFile(midi_file)


# デフォルトのMIDI出力ポートをオープン
with mido.open_output() as outport:
    # 各メッセージを再生しながらループ
    for msg in mid.play():
        # メッセージがノートオンかどうかを確認
        if msg.type == 'note_on':
            # ノート番号を表示
            print(f'Note on: {msg.note}')
        # MIDIメッセージを出力ポートに送信して音を鳴らす
        outport.send(msg)
        # タイミングを合わせるためにメッセージの時間だけ待機
        time.sleep(msg.time if msg.time > 0 else 0)
