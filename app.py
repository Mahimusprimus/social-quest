import streamlit as st
import random
import time

# Set halaman agar tampilannya rapi dan responsif di HP/Laptop
st.set_page_config(page_title="Social Daily Quest", page_icon="🔥", layout="centered")

# DATABASE 100 TANTANGAN SOSIAL (Sama seperti sebelumnya)
BANK_QUEST = [
    # --- EASY (Poin: 50) ---
    {"id": 1, "teks": "Tanyakan jam saat ini kepada orang asing meskipun kamu tahu jam berapa sekarang.", "lokasi": ["Mall", "Studio Musik", "Perpustakaan", "Kafe", "Sekolah", "Taman"], "waktu": ["Pagi", "Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 2, "teks": "Sapa petugas keamanan (satpam) atau barista dengan senyuman dan ucapkan 'Semangat kerjanya, Pak/Kak!'.", "lokasi": ["Mall", "Studio Musik", "Kafe", "Sekolah"], "waktu": ["Pagi", "Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 3, "teks": "Tanyakan arah jalan atau letak toilet terdekat ke orang asing yang sedang berjalan.", "lokasi": ["Mall", "Sekolah", "Taman"], "waktu": ["Pagi", "Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 4, "teks": "Puji sepatu atau pakaian seseorang yang berpapasan denganmu secara tulus (misal: 'Keren sepatunya, Kak!').", "lokasi": ["Mall", "Studio Musik", "Kafe", "Sekolah", "Taman"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 5, "teks": "Tanyakan rekomendasi buku atau area membaca yang tenang kepada pengunjung lain di perpustakaan.", "lokasi": ["Perpustakaan"], "waktu": ["Pagi", "Siang", "Sore"], "kesulitan": "Easy", "poin": 50},
    {"id": 6, "teks": "Ucapkan terima kasih dengan kontak mata yang jelas dan senyuman kepada kasir setelah membayar.", "lokasi": ["Mall", "Kafe"], "waktu": ["Pagi", "Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 7, "teks": "Tahan pintu untuk orang di belakangmu dan berikan anggukan sopan saat mereka lewat.", "lokasi": ["Mall", "Perpustakaan", "Sekolah"], "waktu": ["Pagi", "Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 8, "teks": "Tanyakan kepada seseorang apakah kursi di dekatnya kosong sebelum kamu duduk.", "lokasi": ["Kafe", "Perpustakaan", "Sekolah", "Taman"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 9, "teks": "Pinjam pulpen atau tipe-x ke orang di sebelahmu yang tidak terlalu akrab denganmu.", "lokasi": ["Sekolah", "Perpustakaan"], "waktu": ["Pagi", "Siang", "Sore"], "kesulitan": "Easy", "poin": 50},
    {"id": 10, "teks": "Tanyakan rekomendasi menu minuman paling enak/best-seller kepada pengunjung kafe yang sedang antre.", "lokasi": ["Kafe"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 11, "teks": "Katakan 'Permisi' dengan ramah sambil tersenyum saat melewati sekelompok orang yang sedang berkumpul.", "lokasi": ["Sekolah", "Taman", "Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 12, "teks": "Tanyakan tarif sewa studio atau jadwal kosong terdekat ke penjaga studio musik.", "lokasi": ["Studio Musik"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 13, "teks": "Beri tahu seseorang dengan sopan jika barangnya hampir terjatuh atau talinya lepas.", "lokasi": ["Mall", "Sekolah", "Taman"], "waktu": ["Pagi", "Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 14, "teks": "Tanyakan kepada seseorang yang sedang duduk di taman, apakah cuaca hari ini menurutnya terlalu panas/mendung.", "lokasi": ["Taman"], "waktu": ["Pagi", "Siang", "Sore"], "kesulitan": "Easy", "poin": 50},
    {"id": 15, "teks": "Ucapkan 'Selamat pagi/siang' ke bapak/ibu kantin sebelum memesan makanan.", "lokasi": ["Sekolah"], "waktu": ["Pagi", "Siang"], "kesulitan": "Easy", "poin": 50},
    {"id": 16, "teks": "Tanyakan lokasi spot foto yang paling bagus di area mall ini ke pengunjung lain.", "lokasi": ["Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 17, "teks": "Berikan jalan duluan kepada orang lain saat berebut ingin masuk ke dalam lift atau pintu toko.", "lokasi": ["Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 18, "teks": "Tanyakan ke penjaga perpustakaan di mana letak rak buku fiksi atau komik.", "lokasi": ["Perpustakaan"], "waktu": ["Pagi", "Siang", "Sore"], "kesulitan": "Easy", "poin": 50},
    {"id": 19, "teks": "Sapa teman sekelas yang belum pernah atau jarang sekali mengobrol denganmu secara langsung.", "lokasi": ["Sekolah"], "waktu": ["Pagi", "Siang"], "kesulitan": "Easy", "poin": 50},
    {"id": 20, "teks": "Puji estetika atau desain interior kafe tempat kamu memesan langsung ke baristanya.", "lokasi": ["Kafe"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 21, "teks": "Tanyakan ke seseorang yang sedang memegang brosur/peta di mall, apakah ada event seru hari ini.", "lokasi": ["Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 22, "teks": "Tanyakan merek senar gitar atau stik drum yang paling awet menurut staf penjaga studio.", "lokasi": ["Studio Musik"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 50},
    {"id": 23, "teks": "Saat di taman, sapa seseorang yang sedang membawa hewan peliharaan (seperti kucing/anjing).", "lokasi": ["Taman"], "waktu": ["Pagi", "Sore"], "kesulitan": "Easy", "poin": 50},
    {"id": 24, "teks": "Tanyakan jam operasional perpustakaan sampai jam berapa kepada pengunjung di sebelahmu.", "lokasi": ["Perpustakaan"], "waktu": ["Siang", "Sore"], "kesulitan": "Easy", "poin": 50},
    {"id": 25, "teks": "Ucapkan 'Terima kasih banyak ya' sambil tersenyum lebar kepada tukang parkir setelah merapikan motormu.", "lokasi": ["Kafe", "Mall", "Studio Musik"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Easy", "poin": 25},

    # --- MEDIUM (Poin: 100) ---
    {"id": 26, "teks": "Cari orang yang sedang mendengarkan musik pakai headphone/earphone. Tanyakan dengan sopan lagu apa yang sedang dia dengar.", "lokasi": ["Perpustakaan", "Kafe", "Taman", "Sekolah"], "waktu": ["Pagi", "Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 27, "teks": "Ajak ngobrol seseorang yang sedang mengantre makanan/minuman tentang berapa lama biasanya antrean di tempat ini.", "lokasi": ["Mall", "Kafe", "Sekolah"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 28, "teks": "Tanyakan pendapat seseorang yang sedang memilih buku di rak yang sama denganmu: 'Buku ini bagus gak ya menurutmu?'.", "lokasi": ["Perpustakaan"], "waktu": ["Siang", "Sore"], "kesulitan": "Medium", "poin": 100},
    {"id": 29, "teks": "Dekati orang yang sedang bermain *game* di HP-nya, tanyakan game apa itu dan apakah seru dimainkan.", "lokasi": ["Kafe", "Sekolah", "Taman"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 30, "teks": "Tanyakan kepada seseorang yang membawa hewan peliharaan di taman: 'Boleh saya elus? Namanya siapa?'.", "lokasi": ["Taman"], "waktu": ["Pagi", "Sore"], "kesulitan": "Medium", "poin": 100},
    {"id": 31, "teks": "Diskusikan menu baru dengan barista, tanyakan apa perbedaan rasa menu A dan menu B sebelum kamu memilih.", "lokasi": ["Kafe"], "waktu": ["Pagi", "Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 32, "teks": "Minta rekomendasi toko pakaian cowok/cewek yang bagus dan terjangkau di mall ini kepada sesama pengunjung.", "lokasi": ["Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 33, "teks": "Tanyakan kepada seseorang yang sedang menyendiri di taman, apakah mereka sering datang ke taman ini untuk cari inspirasi.", "lokasi": ["Taman"], "waktu": ["Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 34, "teks": "Ajak bicara teman sekelas yang sedang membaca buku/belajar sendirian saat jam istirahat tentang materi pelajaran tadi.", "lokasi": ["Sekolah"], "waktu": ["Pagi", "Siang"], "kesulitan": "Medium", "poin": 100},
    {"id": 35, "teks": "Tanyakan kepada seseorang yang sedang bermain gitar di studio/kafe tentang berapa lama mereka sudah belajar alat musik tersebut.", "lokasi": ["Studio Musik", "Kafe"], "waktu": ["Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 36, "teks": "Komentari cuaca hari ini yang sangat terik/hujan kepada orang di sebelahmu yang juga sedang berteduh/menunggu.", "lokasi": ["Mall", "Kafe", "Sekolah", "Taman"], "waktu": ["Siang", "Sore"], "kesulitan": "Medium", "poin": 100},
    {"id": 37, "teks": "Minta rekomendasi playlist lagu santai/kerja ke orang yang sedang laptopan di kafe.", "lokasi": ["Kafe"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 38, "teks": "Tanyakan kepada pengunjung mall lain di mana mereka membeli makanan/minuman unik yang sedang mereka bawa.", "lokasi": ["Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 39, "teks": "Ajak kenalan satu orang dari kelas lain yang kebetulan sedang berpapasan atau duduk di dekatmu saat istirahat.", "lokasi": ["Sekolah"], "waktu": ["Pagi", "Siang"], "kesulitan": "Medium", "poin": 100},
    {"id": 40, "teks": "Tanyakan kepada petugas perpus mengenai buku baru yang paling cepat habis dipinjam bulan ini.", "lokasi": ["Perpustakaan"], "waktu": ["Pagi", "Siang", "Sore"], "kesulitan": "Medium", "poin": 100},
    {"id": 41, "teks": "Beri tahu seseorang di kafe bahwa gaya berpakaian (*outfit*)-nya sangat keren dan tanyakan mereka beli kemeja/jaket itu di mana.", "lokasi": ["Kafe", "Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 42, "teks": "Tanyakan kepada musisi/anak band yang sedang *tuning* alat musik di studio: 'Gitar itu tipenya apa ya? Suaranya asik banget.'", "lokasi": ["Studio Musik"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 43, "teks": "Tanyakan kepada seseorang yang sedang berolahraga di taman, apakah ada komunitas lari/olahraga di daerah ini.", "lokasi": ["Taman"], "waktu": ["Pagi", "Sore"], "kesulitan": "Medium", "poin": 100},
    {"id": 44, "teks": "Mintalah bantuan kepada seseorang di mall untuk membantumu memilih hadiah ulang tahun yang netral (seperti tumbler/topi).", "lokasi": ["Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 45, "teks": "Tanyakan kepada seseorang yang sedang memegang kamera di taman/mall, objek apa yang paling seru difoto di sekitar sini.", "lokasi": ["Taman", "Mall"], "waktu": ["Siang", "Sore"], "kesulitan": "Medium", "poin": 100},
    {"id": 46, "teks": "Ajak diskusi singkat orang di sebelahmu di perpustakaan tentang tugas sekolah/kuliah yang menumpuk.", "lokasi": ["Perpustakaan"], "waktu": ["Siang", "Sore"], "kesulitan": "Medium", "poin": 100},
    {"id": 47, "teks": "Tanyakan kepada rombongan anak sekolah lain yang sedang nongkrong tentang es krim atau jajanan apa yang paling enak di dekat sini.", "lokasi": ["Sekolah", "Taman"], "waktu": ["Siang", "Sore"], "kesulitan": "Medium", "poin": 100},
    {"id": 48, "teks": "Tanyakan ke penjaga kafe apakah mereka menyetel lagu sendiri atau menggunakan playlist publik, karena lagunya enak didengar.", "lokasi": ["Kafe"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 49, "teks": "Minta opini singkat dari orang di toko musik tentang perbedaan efek gitar analog dan digital.", "lokasi": ["Studio Musik"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 50, "teks": "Ajak berbincang bapak ojek online atau supir yang sedang menunggu penumpang tentang kondisi jalanan hari ini.", "lokasi": ["Mall", "Kafe", "Sekolah"], "waktu": ["Pagi", "Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 51, "teks": "Tanyakan ke orang asing di mall apakah bioskop hari ini ramai antrean untuk film yang sedang viral.", "lokasi": ["Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 52, "teks": "Tanyakan pada seseorang di taman, jam berapa lampu taman biasanya mulai dinyalakan.", "lokasi": ["Taman"], "waktu": ["Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 53, "teks": "Diskusikan sebuah buku bergenre misteri/thriller dengan orang yang sedang melihat-lihat di rak buku genre yang sama.", "lokasi": ["Perpustakaan"], "waktu": ["Siang", "Sore"], "kesulitan": "Medium", "poin": 100},
    {"id": 54, "teks": "Tanyakan ke orang di sebelahmu saat di kafe, apakah colokan listrik di dekat mereka berfungsi dengan baik.", "lokasi": ["Kafe"], "waktu": ["Pagi", "Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 55, "teks": "Ajak bercanda ringan seseorang yang sedang cemberut/bosan menunggu antrean di kasir.", "lokasi": ["Mall", "Kafe"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 56, "teks": "Tanyakan rekomendasi studio foto atau studio musik yang murah tapi bagus di daerah sekitar sini ke orang asing.", "lokasi": ["Studio Musik", "Kafe"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 57, "teks": "Tanyakan kepada orang asing di sekolah/kampus tentang lokasi ruang guru atau gedung tertentu dengan ramah.", "lokasi": ["Sekolah"], "waktu": ["Pagi", "Siang"], "kesulitan": "Medium", "poin": 100},
    {"id": 58, "teks": "Komentari gambar/stiker yang ada di laptop orang lain yang sedang duduk di kafe (misal stiker band atau game).", "lokasi": ["Kafe"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Medium", "poin": 100},
    {"id": 59, "teks": "Tanyakan pada seseorang yang sedang membaca koran/majalah di perpustakaan tentang berita utama hari ini.", "lokasi": ["Perpustakaan"], "waktu": ["Pagi", "Siang"], "kesulitan": "Medium", "poin": 100},
    {"id": 60, "teks": "Mintalah pendapat seseorang di taman, apakah udara hari ini lebih segar dibanding hari kemarin.", "lokasi": ["Taman"], "waktu": ["Pagi", "Sore"], "kesulitan": "Medium", "poin": 100},

    # --- HARD (Poin: 150) ---
    {"id": 61, "teks": "Cari perempuan yang bisa bermain musik (gitar/piano/dll) dan ajak bicara soal lagu atau musisi favoritnya.", "lokasi": ["Studio Musik", "Kafe", "Sekolah"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 62, "teks": "Cari orang yang penampilannya terlihat 'anak band' atau suka musik alternatif/rock. Puji kaos bandnya dan tanyakan rekomendasi band lokal.", "lokasi": ["Mall", "Studio Musik", "Kafe"], "waktu": ["Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 63, "teks": "Dekati kelompok berisi 2-3 orang asing yang sedang berdiskusi santai, lalu tanyakan opini mereka tentang suatu topik ringan.", "lokasi": ["Kafe", "Taman", "Sekolah"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 64, "teks": "Duduk di sebelah orang yang tidak kamu kenal di kantin/kafe, ajak mengobrol dari awal berkenalan hingga tahu kesibukannya.", "lokasi": ["Kafe", "Sekolah"], "waktu": ["Siang", "Sore"], "kesulitan": "Hard", "poin": 150},
    {"id": 65, "teks": "Tanyakan kepada seseorang yang sedang bermain skate/sepeda di taman, apakah melelahkan mempelajari trik tersebut dan minta tips dasar.", "lokasi": ["Taman"], "waktu": ["Sore"], "kesulitan": "Hard", "poin": 150},
    {"id": 66, "teks": "Minta izin untuk duduk satu meja dengan orang asing di kafe yang penuh, lalu bangun percakapan hingga suasana cair.", "lokasi": ["Kafe"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 67, "teks": "Ajak bicara orang yang sedang memajang karya/seni/bermain musik jalanan, tanyakan motivasi dan proses kreatif mereka.", "lokasi": ["Mall", "Taman"], "waktu": ["Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 68, "teks": "Tanyakan kepada seseorang yang terlihat seumuran di mall, rekomendasi film bioskop yang seru minggu ini dan kenapa harus nonton itu.", "lokasi": ["Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 69, "teks": "Dekati orang asing di studio musik, ajak bicara tentang genre Shoegaze atau Indie Rock, dan tanyakan apakah mereka punya band.", "lokasi": ["Studio Musik"], "waktu": ["Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 70, "teks": "Cari orang yang sedang membaca novel tebal di perpustakaan/kafe, tanyakan plotnya tanpa memberikan spoiler.", "lokasi": ["Perpustakaan", "Kafe"], "waktu": ["Siang", "Sore"], "kesulitan": "Hard", "poin": 150},
    {"id": 71, "teks": "Ajak mengobrol kakak kelas atau murid yang terkenal aktif di sekolah mengenai tips berorganisasi atau kepanitiaan acara.", "lokasi": ["Sekolah"], "waktu": ["Pagi", "Siang"], "kesulitan": "Hard", "poin": 150},
    {"id": 72, "teks": "Tanyakan pendapat orang asing di mall tentang tren fashion saat ini, apakah menurut mereka keren atau aneh.", "lokasi": ["Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 73, "teks": "Saat di kafe, ajak seseorang berdiskusi tentang kopi pahit vs kopi manis, lalu tebak kepribadian mereka dari jenis kopi kesukaannya.", "lokasi": ["Kafe"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 74, "teks": "Dekati seseorang di taman yang sedang menggambar/sketsa, puji karyanya dan tanyakan sudah berapa lama menekuni hobi itu.", "lokasi": ["Taman"], "waktu": ["Siang", "Sore"], "kesulitan": "Hard", "poin": 150},
    {"id": 75, "teks": "Tanyakan kepada sesama pemusik di studio tentang bagaimana cara mengatasi rasa gugup atau demam panggung sebelum tampil.", "lokasi": ["Studio Musik"], "waktu": ["Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 76, "teks": "Ajak berkenalan orang asing yang sedang sendirian di sudut mall, tanyakan apakah mereka sedang menunggu seseorang.", "lokasi": ["Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 77, "teks": "Ajak mengobrol seseorang di perpus yang sedang mencari buku sejarah/sains, tanyakan topik spesifik apa yang sedang mereka riset.", "lokasi": ["Perpustakaan"], "waktu": ["Siang", "Sore"], "kesulitan": "Hard", "poin": 150},
    {"id": 78, "teks": "Temukan seseorang yang memakai merchandise anime/game, diskusikan episode terbaru atau update game tersebut dengannya.", "lokasi": ["Kafe", "Mall", "Sekolah"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 79, "teks": "Ajak bicara seseorang di kafe mengenai maraknya budaya WFC (Work From Cafe) dan tanyakan apakah mereka lebih produktif di rumah atau kafe.", "lokasi": ["Kafe"], "waktu": ["Pagi", "Siang", "Sore"], "kesulitan": "Hard", "poin": 150},
    {"id": 80, "teks": "Diskusikan sebuah alat musik langka atau mahal dengan pengunjung lain di toko alat musik/studio musik.", "lokasi": ["Studio Musik"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 81, "teks": "Ajak kenalan orang asing di taman dan tanyakan impian terbesar atau rencana liburan mereka dalam waktu dekat.", "lokasi": ["Taman"], "waktu": ["Pagi", "Sore"], "kesulitan": "Hard", "poin": 150},
    {"id": 82, "teks": "Mintalah seseorang di mall memberi nilai dari 1-10 untuk outfit yang kamu pakai hari ini, lalu tanyakan alasannya.", "lokasi": ["Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 83, "teks": "Ajak mengobrol seseorang yang sedang melihat pameran foto/lukisan di mall tentang makna karya seni tersebut.", "lokasi": ["Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 84, "teks": "Tanyakan kepada seseorang di kafe tentang rekomendasi tempat hunting foto atau nongkrong tersembunyi (*hidden gem*) di kota ini.", "lokasi": ["Kafe"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Hard", "poin": 150},
    {"id": 85, "teks": "Ajak bicara staf atau panitia sebuah acara di mall/sekolah tentang kesibukan di balik layar merancang acara tersebut.", "lokasi": ["Mall", "Sekolah"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Hard", "poin": 150},

    # --- EXPERT (Poin: 250) ---
    {"id": 86, "teks": "Minta orang asing secara acak untuk memilihkan satu menu makanan/minuman misteri untukmu di kasir, dan kamu wajib membelinya.", "lokasi": ["Kafe", "Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Expert", "poin": 250},
    {"id": 87, "teks": "Gabung ke sekelompok orang asing yang sedang asyik mengobrol di kafe/taman setelah meminta izin dengan sopan, lalu ikut mengobrol minimal 5 menit.", "lokasi": ["Kafe", "Taman"], "waktu": ["Sore", "Malam"], "kesulitan": "Expert", "poin": 250},
    {"id": 88, "teks": "Tanyakan ke orang asing: 'Kalau kamu punya waktu 1 jam sebelum dunia kiamat, apa yang mau kamu lakuin?', dengarkan ceritanya.", "lokasi": ["Kafe", "Taman", "Mall"], "waktu": ["Sore", "Malam"], "kesulitan": "Expert", "poin": 250},
    {"id": 89, "teks": "Ajak seseorang yang belum dikenal sama sekali untuk bermain game batu-gunting-kertas. Jika kamu menang, dia harus kasih rekomendasi 1 lagu.", "lokasi": ["Sekolah", "Mall", "Taman"], "waktu": ["Siang", "Sore"], "kesulitan": "Expert", "poin": 250},
    {"id": 90, "teks": "Pinjam korek api atau tanyakan tempat merokok ke sekumpulan anak punk/anak band rock, lalu ajak mereka mengobrol tentang skena musik lokal.", "lokasi": ["Studio Musik", "Taman"], "waktu": ["Sore", "Malam"], "kesulitan": "Expert", "poin": 250},
    {"id": 91, "teks": "Tanyakan kepada seseorang yang sedang sendirian: 'Menurutmu, apa hal paling berharga dalam sebuah pertemanan?', dengarkan baik-baik filosofinya.", "lokasi": ["Perpustakaan", "Kafe", "Taman"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Expert", "poin": 250},
    {"id": 92, "teks": "Mintalah seseorang menceritakan lelucon/jokes paling lucu yang mereka tahu, dan tertawalah bersama mereka.", "lokasi": ["Sekolah", "Kafe", "Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Expert", "poin": 250},
    {"id": 93, "teks": "Datangi seseorang yang terlihat sangat lelah atau stres, berikan satu permen atau minuman botol kemasan baru, lalu beri kata-kata penyemangat.", "lokasi": ["Mall", "Sekolah", "Taman"], "waktu": ["Siang", "Sore"], "kesulitan": "Expert", "poin": 250},
    {"id": 94, "teks": "Lakukan 'jamming' atau bernyanyi bersama orang asing yang sedang memainkan alat musik di studio atau tempat umum.", "lokasi": ["Studio Musik", "Taman"], "waktu": ["Sore", "Malam"], "kesulitan": "Expert", "poin": 250},
    {"id": 95, "teks": "Tanyakan kepada seseorang yang usianya jauh lebih tua di taman tentang nasihat hidup terbaik apa yang bisa mereka berikan untuk anak muda.", "lokasi": ["Taman"], "waktu": ["Pagi", "Sore"], "kesulitan": "Expert", "poin": 250},
    {"id": 96, "teks": "Minta orang asing mengajarimu satu patah kata atau kalimat dari bahasa daerah mereka yang belum kamu ketahui artinya.", "lokasi": ["Kafe", "Sekolah", "Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Expert", "poin": 250},
    {"id": 97, "teks": "Ajak orang asing bertukar akun sosial media (Instagram/Letterboxd/Spotify) setelah mengobrol seru minimal 3 menit tentang hobi yang sama.", "lokasi": ["Kafe", "Studio Musik", "Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Expert", "poin": 250},
    {"id": 98, "teks": "Wawancarai singkat pengunjung mall acak mengenai pendapat mereka tentang penggunaan AI (Artificial Intelligence) di masa kini.", "lokasi": ["Mall"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Expert", "poin": 250},
    {"id": 99, "teks": "Dekati orang asing yang sedang membaca buku psikologi/self-improvement, tanyakan tips terbesar dari buku itu untuk mengatasi kecemasan sosial.", "lokasi": ["Perpustakaan", "Kafe"], "waktu": ["Siang", "Sore"], "kesulitan": "Expert", "poin": 250},
    {"id": 100, "teks": "Beranikan diri meminta foto bersama dengan seseorang yang baru saja selesai kamu ajak mengobrol panjang (orang asing total) sebagai kenang-kenangan quest.", "lokasi": ["Mall", "Studio Musik", "Kafe", "Taman", "Sekolah"], "waktu": ["Siang", "Sore", "Malam"], "kesulitan": "Expert", "poin": 250}
]

# Inisialisasi Session State (Sistem memori agar data website tidak hilang saat di-refresh)
if "total_poin" not in st.session_state:
    st.session_state.total_poin = 0
if "quest_aktif" not in st.session_state:
    st.session_state.quest_aktif = None
if "status_game" not in st.session_state:
    st.session_state.status_game = "menu"  # menu, quest_running, form_pembuktian

# --- TAMPILAN HEADER WEBSITE ---
st.title("🔥 Real-Life Social Daily Quest")
st.subheader("Ubah dunia nyata jadi RPG dan latih skill sosialmu!")

# Tampilkan Poin Pemain di Pojok Atas/Sidebar
st.sidebar.metric(label="🏆 TOTAL POIN KAMU", value=st.session_state.total_poin)
st.sidebar.markdown("---")
st.sidebar.info("Aplikasi ini dibuat khusus untuk uji coba personal. Selesaikan tantangan dalam waktu 1 jam!")

# --- KONDISI 1: MENU UTAMA / SETTING ---
if st.session_state.status_game == "menu":
    st.write("### ⚙️ Set Kondisi Kamu Sekarang")
    
    col1, col2 = st.columns(2)
    with col1:
        lokasi_user = st.selectbox("Kamu lagi di mana?", ["Mall", "Studio Musik", "Perpustakaan", "Kafe", "Sekolah", "Taman"])
    with col2:
        waktu_user = st.selectbox("Sekarang jam/waktu bagian apa?", ["Pagi", "Siang", "Sore", "Malam"])
        
    if st.button("🎲 Cari Tantangan (Roll Quest)", type="primary", use_container_width=True):
        # Filter Quest
        quest_cocok = [
            q for q in BANK_QUEST 
            if lokasi_user in q["lokasi"] and waktu_user in q["waktu"]
        ]
        
        if quest_cocok:
            st.session_state.quest_aktif = random.choice(quest_cocok)
            st.session_state.status_game = "quest_running"
            st.rerun()
        else:
            st.error("😔 Maaf, tidak ada quest yang cocok untuk kombinasi tersebut. Coba ganti lokasi!")

# --- KONDISI 2: QUEST SEDANG BERJALAN ---
elif st.session_state.status_game == "quest_running":
    q = st.session_state.quest_aktif
    
    st.warning(f"### 🎯 TANTANGAN AKTIF: [{q['kesulitan']}]")
    st.info(f"👉 **\"{q['teks']}\"**")
    st.write(f"💰 **Hadiah:** {q['poin']} Base Poin")
    
    st.markdown("---")
    st.write("⏱️ **Waktu Kamu: 1 Jam di Dunia Nyata.**")
    st.write("Keluar ke dunia nyata sekarang dan lakukan aksinya! Jika sudah selesai atau gagal, kembali ke halaman web ini.")
    
    col3, col4 = st.columns(2)
    with col3:
        if st.button("✅ SAYA BERHASIL", type="success", use_container_width=True):
            st.session_state.status_game = "form_pembuktian"
            st.rerun()
    with col4:
        if st.button("❌ SAYA GAGAL / MENYERAH", type="danger", use_container_width=True):
            st.session_state.total_poin -= 30
            st.error("Quest Gagal! Poin kamu dipotong -30. Jangan menyerah, coba lagi nanti!")
            time.sleep(2)
            st.session_state.status_game = "menu"
            st.session_state.quest_aktif = None
            st.rerun()

# --- KONDISI 3: FORM PEMBUKTIAN & SIMULASI PENILAIAN ---
elif st.session_state.status_game == "form_pembuktian":
    q = st.session_state.quest_aktif
    st.write("### 📸 Form Pembuktian Quest")
    
    # Input Bukti sesuai kesepakatan
    file_foto = st.file_uploader("Upload Foto Bareng / Bukti Pendukung", type=["jpg", "jpeg", "png"])
    info_didapat = st.text_area("Informasi apa saja yang kamu dapat dari orang tersebut secara singkat?", placeholder="Contoh: Nama dia Salsa, dia suka genre musik shoegaze dan main bass...")
    
    # Simulasi estimasi waktu pengerjaan untuk bonus kecepatan
    menit_pengerjaan = st.slider("Berapa menit waktu yang kamu habiskan untuk menyelesaikan quest ini?", 1, 90, 25)
    
    if st.button("🚀 Kirim & Hitung Skor Poin", type="primary", use_container_width=True):
        if not info_didapat:
            st.error("Form info singkat wajib diisi sebagai bukti interaksi sosial!")
        else:
            # Hitung kalkulasi skor
            bonus_kecepatan = 0
            if menit_pengerjaan <= 20:
                bonus_kecepatan = 50
                st.balloons()
                st.success("⚡ Luar biasa! Sangat Cepat! Kamu dapat bonus +50 Poin!")
            elif menit_pengerjaan <= 40:
                bonus_kecepatan = 25
                st.success("🏃 Cepat dan Sigap! Kamu dapat bonus +25 Poin!")
            elif menit_pengerjaan <= 60:
                st.success("👍 Tepat Waktu! Kamu menyelesaikan quest di bawah 1 jam.")
            else:
                st.session_state.total_poin -= 30
                st.error("⚠️ Meskipun selesai, kamu melebihi batas waktu 1 jam. Quest dianggap expired (-30 Poin).")
                time.sleep(2)
                st.session_state.status_game = "menu"
                st.session_state.quest_aktif = None
                st.rerun()
                
            total_masuk = q['poin'] + bonus_kecepatan
            st.session_state.total_poin += total_masuk
            
            st.toast(f"Sukses mencatat bukti! +{total_masuk} Poin masuk.", icon='💰')
            time.sleep(3)
            
            # Reset Status Game ke Menu Utama
            st.session_state.status_game = "menu"
            st.session_state.quest_aktif = None
            st.rerun()