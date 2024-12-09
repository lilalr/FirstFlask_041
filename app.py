from flask import Flask, request, render_template

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk menangani data dari form
@app.route('/submit', methods=['POST'])
def submit():
    # Mengambil data dari form
    name = request.form.get('nama')
    major = request.form.get('prodi')
    year = request.form.get('angkatan')

    return f"Nama: {name}, Prodi: {major}, Angkatan: {year}"

if __name__ == '__main__':
    app.run(debug=True)
