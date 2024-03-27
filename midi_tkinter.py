import tkinter as tk
from tkinter import filedialog, scrolledtext
import mido
import time

class MidiPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('MIDI Player')

        # ファイル選択ボタン
        self.open_button = tk.Button(self.root, text='ファイルを選択', command=self.open_file)
        self.open_button.pack(pady=20)

        # 実行ボタン
        self.play_button = tk.Button(self.root, text='実行', command=self.play_midi)
        self.play_button.pack(pady=20)

        # メッセージ表示用のTextウィジェット
        self.text_widget = scrolledtext.ScrolledText(self.root, height=10)
        self.text_widget.pack(pady=20)

        # MIDIファイルのパスを保持する変数
        self.midi_file_path = ''

    def open_file(self):
        """ファイル選択ダイアログを開く"""
        self.midi_file_path = filedialog.askopenfilename(filetypes=[('MIDI files', '*.mid')])
        print(f'選択されたファイル: {self.midi_file_path}')

    def play_midi(self):
        """MIDIファイルを再生"""
        if self.midi_file_path:
            try:
                mid = mido.MidiFile(self.midi_file_path)
                # MIDIファイルの処理コード（コメントアウトされた部分を含む）
                with mido.open_output() as outport:
                    for msg in mid.play():
                        if msg.type == 'note_off':
                            message = f'Note: {msg.note}\nTime: {msg.time * 1600}\n-------\n'
                            self.text_widget.insert(tk.END, message)
                        outport.send(msg)
                        time.sleep(msg.time if msg.time > 0 else 0)
            except Exception as e:
                print(f'エラーが発生しました: {e}')
        else:
            print('ファイルが選択されていません。')

if __name__ == '__main__':
    root = tk.Tk()
    app = MidiPlayerApp(root)
    root.mainloop()
