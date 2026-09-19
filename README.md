# Refactoring Tugas: Memecah Monolith Python

Repository ini berisi hasil refactoring dari `app.py` (monolith) menjadi beberapa module dengan tanggung jawab yang lebih jelas.

## 1. Dependency Map

### 1.1 Sebelum Refactoring (Monolith)

Sebelum refactoring, seluruh kode berada dalam satu file `app.py`. Domain logic, storage, dan CLI saling terhubung tanpa abstraksi.

**Hubungan antar fungsi:**
main → create_user
create_user → load_users
create_user → validate_user
create_user → save_users
list_users → load_users
load_users → users.json
save_users → users.json


**Diagram dependency:**
┌─────────────────────────────────────────────┐
│ app.py │
│ │
│ ┌──────────┐ │
│ │ main │ │
│ └────┬─────┘ │
│ │ │
│ ↓ │
│ ┌──────────────┐ │
│ │ create_user │ │
│ └──┬────┬───┬──┘ │
│ │ │ │ │
│ ↓ ↓ ↓ │
│ ┌──────┐ │ ┌────────┐ │
│ │load_ │ │ │save_ │ │
│ │users │ │ │users │ │
│ └───┬──┘ │ └───┬────┘ │
│ │ │ │ │
│ │ ↓ │ │
│ │ ┌────────────┐ │
│ │ │validate_ │ │
│ │ │user │ │
│ │ └────────────┘ │
│ │ │
│ ↓ │
│ ┌─────────────┐ │
│ │ users.json │ │
│ └─────────────┘ │
│ │
│ ┌───────────┐ │
│ │list_users │──→ load_users() ──→ json │
│ └───────────┘ │
└─────────────────────────────────────────────┘

text

**Karakteristik:**
- Domain logic (`create_user`, `validate_user`) bergantung langsung ke storage (`load_users`, `save_users`)
- CLI (`main`) bergantung langsung ke domain
- Tidak ada abstraksi/interface
- Sulit di-test karena semua tergantung file JSON

### 1.2 Sesudah Refactoring (Modular)

Setelah refactoring, dependency menjadi satu arah dan bersih.

**Hubungan antar module:**
main.py → UserService
main.py → JsonUserStorage
UserService → UserStorage (interface)
UserService → validate_user
JsonUserStorage → UserStorage (implements)
JsonUserStorage → users.json
validate_user → (tidak depend ke apa pun)

text

**Diagram dependency:**
┌─────────────────────────────┐
│ main.py │
│ (Presentation) │
│ │
│ main() → UserService │
│ main() → JsonUserStorage │
└──────────────┬──────────────┘
│
↓
┌─────────────────────────────┐
│ services/user_service.py │
│ (Domain Logic) │
│ │
│ UserService(storage) │
│ └→ validate_user │
└──────────────┬──────────────┘
│ depends on
↓
┌─────────────────────────────┐
│ storage/user_storage.py │
│ (Interface / Port) │
│ │
│ class UserStorage(ABC) │
└──────────────┬──────────────┘
↑ implements
│
┌─────────────────────────────┐
│ storage/json_storage.py │
│ (Adapter) │
│ │
│ JsonUserStorage(UserStorage)│
└──────────────┬──────────────┘
↓
users.json

┌─────────────────────────────┐
│ domain/user.py │
│ validate_user() │
│ (tidak depend ke apa pun) │
└─────────────────────────────┘

text

### 1.3 Penjelasan Perubahan Dependency

**Perubahan utama:**

| Aspek | Sebelum | Sesudah |
|-------|---------|---------|
| Arah dependency | Bercampur dalam satu file | Satu arah: CLI → Service → Interface ← Adapter |
| Domain ↔ Storage | Langsung ke fungsi konkret | Lewat abstraksi `UserStorage` |
| Abstraksi | Tidak ada | Ada ABC `UserStorage` |
| Jumlah file | 1 file (`app.py`) | 5 module terpisah |
| Testability | Sulit (harus ada file JSON) | Mudah (bisa pakai fake storage) |

**Narasi penjelasan:**

Sebelum refactoring, semua fungsi berada dalam satu file `app.py`. Domain logic (`create_user`, `validate_user`) bergantung langsung pada detail storage (`load_users`, `save_users`). Akibatnya, perubahan pada storage (misalnya dari JSON ke database) akan memaksa perubahan pada domain logic. Selain itu, CLI (`main`) juga bergantung langsung pada domain, sehingga sulit di-test secara terpisah.

Sesudah refactoring, dependency menjadi satu arah dan bersih:
- `main.py` (CLI) hanya bergantung pada `UserService` dan `JsonUserStorage`
- `UserService` (domain logic) bergantung pada abstraksi `UserStorage`, bukan implementasi konkret
- `JsonUserStorage` (adapter) mengimplementasikan `UserStorage` dan menangani detail file JSON
- `validate_user` di `domain/user.py` berdiri sendiri, tidak bergantung ke apa pun

Perubahan ini menerapkan **Dependency Inversion Principle**: domain tidak lagi bergantung pada detail teknis, melainkan pada abstraksi. Akibatnya:
1. Domain logic bisa di-test tanpa menyentuh file JSON
2. Storage bisa diganti (JSON → database) tanpa mengubah domain
3. CLI bisa diganti (terminal → web) tanpa mengubah domain

## 2. Pemisahan Module

*(akan diisi pada step berikutnya)*

## 3. Test

*(akan diisi pada step berikutnya)*

