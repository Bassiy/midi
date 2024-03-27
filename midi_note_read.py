import mido

# MIDIファイルを開く
mid = mido.MidiFile('yusha_level1.mid')

# トラックごとにメッセージを読む
for track in mid.tracks:
    print(f'Track: {track.name}')
    for msg in track:
        # ノートオンメッセージを探す
        if msg.type == 'note_on':
            print(f'Note: {msg.note}')
