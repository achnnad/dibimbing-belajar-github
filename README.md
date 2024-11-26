Screenshot :

1. Create repo in github
   klik button new repo
   ![1_create_repo_1](https://github.com/user-attachments/assets/3d17411a-3e1b-4c58-b70b-b78d58d59316)
   isi nama repo dengan **dibimbing-belajar-github** kemudian klik create repo
   ![1_create_repo_2](https://github.com/user-attachments/assets/3e4f4f12-080e-452c-a741-1b0edff955e1)
2. Clone repo from github
   ketikkan perintah _git clone <url_repo>_
   ![2_git_clone_1](https://github.com/user-attachments/assets/44f82cdc-e0f7-498e-abbb-6d8ab0917f98)
3. Create python to read csv file
   jalankan perintah **py nama_file.py** untuk menguji fungsionalitas kode
   ![3_read_csv_1](https://github.com/user-attachments/assets/52cd709b-2313-4730-a222-d326236b4e47)
4. Create new branch
   jalankan perintah _git checkout -b <nama_branch>_
   ![4_create_new_branch_1](https://github.com/user-attachments/assets/8ff52629-86c5-44e5-99fa-5b689f22f26f)
   tambahkan file ke staging area dengan perintah _git add <nama_file>_ kemudian lakukan commit dengan perintah _git commit -m "pesan commit"_
   ![5_commit_1](https://github.com/user-attachments/assets/dba0b5aa-6ddc-4f0d-b417-5617df09c8cf)
   kirimkan perubahan ke remote repo dengan perintah _git push <nama_remote_repo> <nama_branch>_
   ![5_commit_2](https://github.com/user-attachments/assets/d0d05161-9c28-4fb0-8efc-8d9746abc050)
   ![5_push_1](https://github.com/user-attachments/assets/662d3af6-225a-4604-a462-b2663e951aa9)
5. Pull Request github
   klik _compare and pull request_
   ![6_pull_request_1](https://github.com/user-attachments/assets/a455be54-1791-4032-ab4a-8a81212e4b90)
   klik _pull request_
   ![6_pull_request_2](https://github.com/user-attachments/assets/78a40cfe-467c-438f-9182-028157fe71b0)
   klik _merge pull request_, jika memang sudah tidak ada conflict
   ![6_pull_request_3](https://github.com/user-attachments/assets/6b894878-5f03-4290-b1da-9099e139676b)
   ![6_pull_request_4](https://github.com/user-attachments/assets/17610150-99fa-487d-8fc3-8223ea278b03)
7. Pull remote main branch
   cek apakah ada perubahan dengan remote repo dengan perintah _git fetch <nama_remote_repo>_
   kemudian check status dengan perintah _git status_, jika ditemukan perbedaan maka lakukan perintah _git puLL <nama_remote_repo> <nama_branch>_
    ![7_pull_remote_1](https://github.com/user-attachments/assets/09ce4103-d78f-4088-80d5-893cd8cea784)
