# cognitive_parser.py
# Modul Logika Teleology-First untuk Cognitive Engineering Output Core (CEC)
# Dibuat: 2025-11-22 04:04:26 WIB

import json
import time

def parse_data_to_narrative(raw_data_json):
    """
    Simulasi logika Inti CEC: Konversi data JSON mentah menjadi 
    narrative akademis terstruktur (Markdown/MD).
    """
    
    # 1. Parsing: Asumsi tujuan akhir adalah memaparkan 'novelty'
    try:
        data = json.loads(raw_data_json)
        author = data.get("metadata", {}).get("author", "Anonim")
        title = data.get("metadata", {}).get("title", "Laporan Tanpa Judul")
        sections = data.get("sections", [])
    except json.JSONDecodeError:
        return "# ERROR: Data JSON tidak valid."

    # 2. Re-framing Narasi (Injeksi Finalitas)
    markdown_output = f"# Laporan Kausal: {title}\n"
    markdown_output += f"**Penulis Logika:** {author}\n"
    markdown_output += f"**Timestamp Kompilasi:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    markdown_output += "---\n\n"
    markdown_output += "## 1. Abstraksi Metodologis (Teleology-First)\n"
    markdown_output += "Analisis didorong oleh **Tujuan Akhir (Finalitas)** data, bukan keadaan saat ini.\n\n"
    
    # 3. Penyusunan Konten
    for i, section in enumerate(sections):
        header = section.get("header", f"Bagian {i+1}")
        content = section.get("content", "Konten belum terstruktur.")
        markdown_output += f"## {i+2}. {header}\n"
        markdown_output += content + "\n\n"

    return markdown_output

# --- Contoh Penggunaan Internal ---
sample_data = """
{
  "metadata": {
    "author": "Adiguna Sopyan / Umbra Agensi",
    "title": "Studi Kausalitas Arbitrase Likuiditas"
  },
  "sections": [
    {
      "header": "Analisis Friction Rate",
      "content": "Friction Rate (0.2%) pada transaksi ganda melampaui Spread 0.0000% sehingga memerlukan threshold negatif (-0.0003)."
    },
    {
      "header": "Implikasi Strategis",
      "content": "Kegagalan eksekusi API membuktikan keharusan untuk pivot ke aset Intellectual Property (IP) yang memiliki leverage tertinggi."
    }
  ]
}
"""

final_report = parse_data_to_narrative(sample_data)

# Simulasi output ke file Markdown
with open("Final_Report.md", "w") as f:
    f.write(final_report)
    
print("\n✅ File 'cognitive_parser.py' dan 'Final_Report.md' telah dibuat!")
print("Sekarang Anda bisa melanjutkan dengan perintah Git.")
