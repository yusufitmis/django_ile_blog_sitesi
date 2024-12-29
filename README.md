# Django Blog Sitesi

Bu proje, kullanıcıların blog postları oluşturup paylaşabileceği, diğer kullanıcıların paylaşımlarını görebileceği ve çeşitli filtreleme özellikleri ile postları sıralayabileceği bir Django tabanlı blog sitesidir.

This project is a Django-based blog site where users can create and share blog posts, view posts from other users, and sort posts using various filters.

## Özellikler / Features

### Kullanıcı İşlemleri / User Operations
- Kullanıcı kaydolma ve giriş yapma.
- E-posta ve şifre doğrulama (şifre uzunluğu kontrolü, hataların kullanıcıya gösterilmesi).
- Kullanıcı profil bilgilerini güncelleyebilme.

- User registration and login.
- Email and password validation (password length checks, displaying errors to the user).
- Ability to update user profile information.

### Blog İşlemleri / Blog Operations
- Anasayfada tüm kullanıcıların postlarının görüntülenmesi.
- Post başlığı ve oluşturulma tarihine göre filtreleme.
- Yeni blog postları oluşturma (başlık ve içerik girilerek paylaşma).

- Viewing all users' posts on the homepage.
- Filtering posts by title and creation date.
- Creating new blog posts (entering title and content to share).

## Projenin Önizlemesi / Project Preview

### 1. Anasayfa / Homepage
![Anasayfa](https://github.com/yusufitmis/django_ile_blog_sitesi/blob/main/home.PNG)

### 2. Giris Yap / Login
![Post Oluşturma](https://github.com/yusufitmis/django_ile_blog_sitesi/blob/main/login.PNG)

### 3. Kayıt Ol / Sign Up
![Post Filtreleme](https://github.com/yusufitmis/django_ile_blog_sitesi/blob/main/signup.PNG)

### 4. Profil Güncelleme / Update Profile
![Profil Güncelleme](https://github.com/yusufitmis/django_ile_blog_sitesi/blob/main/profile.PNG)

## Kurulum / Setup

### Gereksinimler / Requirements
- Python 3.x
- Django 4.x
- Virtualenv (isteğe bağlı / optional)

### Adımlar / Steps

1. **Depoyu klonlayın / Clone the repository**
   ```bash
   git clone https://github.com/kullanici-adi/django-blog.git
   cd django-blog
   ```

2. **Sanallaştırılmış ortamı oluşturun (isteğe bağlı) / Create a virtual environment (optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Gerekli paketleri yükleyin / Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Veritabanını oluşturun / Create the database**
   ```bash
   python manage.py migrate
   ```

5. **Geliştirme sunucusunu çalıştırın / Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Projeyi tarayıcıda açın / Open the project in your browser**
   ```
   http://127.0.0.1:8000/
   ```

## Kullanım / Usage

1. **Kayıt Olma ve Giriş Yapma / Register and Log In:** Yeni kullanıcı oluşturun ya da mevcut bilgilerinizle giriş yapın.
2. **Post Paylaşma / Create a Post:** Anasayfadan "Yeni Post" butonunu kullanarak başlık ve içerik ekleyin.
3. **Filtreleme / Filter Posts:** Postları başlık veya tarih sırasına göre filtreleyin.
4. **Profil Güncelleme / Update Profile:** Profil sekmesinden kullanıcı bilgilerinizi güncelleyin.

## Katkıda Bulunma / Contributing
Projeye katkıda bulunmak için:

To contribute to the project:

1. Bu projeyi forklayın.
   Fork this repository.

2. Kendi dalınızı oluşturun (`git checkout -b feature/ozellik-adi`).
   Create your branch (`git checkout -b feature/feature-name`).

3. Değişikliklerinizi commit edin (`git commit -m 'Yeni bir özellik eklendi'`).
   Commit your changes (`git commit -m 'Added a new feature'`).

4. Dalınıza push edin (`git push origin feature/ozellik-adi`).
   Push to your branch (`git push origin feature/feature-name`).

5. Bir Pull Request oluşturun.
   Create a Pull Request.

## Lisans / License
Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
Proje ile ilgili sorularınız için [kullanici-adi@example.com](mailto:kullanici-adi@example.com) adresine ulaşabilirsiniz.

For questions about the project, contact [username@example.com](mailto:username@example.com).

 
