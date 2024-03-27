import mido
import time

# MIDIファイルを開く
mid = mido.MidiFile('yusha_level1.mid')



"""
# トラックごとにメッセージを読む
for i,track in enumerate(mid.tracks):
    print(f'Track{i}: {track.name}')
    for msg in track:
        # ノートオフメッセージを探す
        if msg.type == 'note_off':
            print(f'Note: {msg.note}')  
            print(f'Time: {msg.time}')
            print("-------")
"""
        
# デフォルトのMIDI出力ポートをオープン
with mido.open_output() as outport:
    # 各メッセージを再生しながらループ
    for msg in mid.play():
        # メッセージがノートオンかどうかを確認
        if msg.type == 'note_off':
            # ノート番号を表示
            print(f'Note: {msg.note}')
            print(f'Time: {msg.time * 1600}')
            print("-------")
        # MIDIメッセージを出力ポートに送信して音を鳴らす
        outport.send(msg)
        # タイミングを合わせるためにメッセージの時間だけ待機
        time.sleep(msg.time if msg.time > 0 else 0)