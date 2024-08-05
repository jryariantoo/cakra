Proyek ini terdiri dari dua tugas utama. Pada tugas pertama, saya mengembangkan aplikasi yang memanfaatkan model AI untuk menghasilkan pertanyaan pilihan ganda berdasarkan konten dokumen. Aplikasi ini dirancang menggunakan Flask untuk antarmuka web dan Gradio untuk inferensi model.

Pada tugas pertama, saya melakukan hit ke untuk mendapatkan response dari request yang ditentukan. Saya menggunakan prompt engineering untuk melakukan hasil yang sesuai, yaitu 5 pertanyaan dengan 4 pilihan ganda dari dokumen yang diunggah.

Pada tugas kedua, saya melakukan analisis data dan membangun model prediksi kualitas jeruk menggunakan dataset yang disediakan. Proses ini melibatkan data cleaning, train & eval model dan lain-lain. Model yang digunakan adalah Random Forest dan XGBoost. Saya tidak menggunakan feature engineering seperti menambhkan kolom, karena setelah di-test malah makin memburuk. Model terbaik kemudian diterapkan dalam aplikasi Gradio untuk memprediksi kualitas jeruk berdasarkan input fitur yang relevan.

Link repositori dan aplikasi yang live:

notebook:
https://colab.research.google.com/drive/1XQ_N4KJ7jypvfStOvqCYneRJnyfENelF?usp=sharing

gradio:
https://16f8e5d605bf46a9c0.gradio.live/

if gradio's link expired, regenerate in notebook.
