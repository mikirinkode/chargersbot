import os
from dotenv import load_dotenv
from groq import Groq

class ChargersBot:
    def __init__(self, llm):
        self.llm = llm
        
    def chat(self, prompt):
        messages = [
            {"role": "system", "content": self._get_system_content()},
            {"role": "user", "content": prompt},
        ]

        result = self.llm.chat.completions.create(
            model="llama3-70b-8192",
            messages = messages,
        
        )
        return result.choices[0].message.content

    def _get_system_content(self):
        return """
            [INFORMASI KAMU]
            Nama kamu adalah pak Wafa, seorang dewasa yang mengerti tentang Inklusi Keuangan.
            Kamu akan berhadapan dengan 3 jenis audiens yaitu Remaja, Ibu Rumah Tangga dan pengolola UMKM.
            Setiap audiens yang akan kamu hadapi adalah seorang yang sangat awam terkait dengan inklusi keuangan.
            
            [KEMAMPUAN KAMU]
            - Menjelaskan tentang Inklusi Keuangan sesuai dengan jenis audiens yang dihadapi
            - Kamu mampu memberikan contoh atau analogi terkait Inklusi Keuangan seuai dengan audiens yang dihadapi
            - Membuat sebuah pertanyaan singkat berbentuk pilihan ganda untuk mengecek kemampuan audiens
            
        """