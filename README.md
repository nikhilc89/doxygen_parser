# Doxygen Pipeline and Log Parser

## How did you test your pipelines?
Pipeline Testing: The .gitlab-ci.yml file was pushed to the repository. This file defines all the steps, including cloning repositories, running commands (like Doxygen), and executing the Python script.

## How did you test repoC Python?
RepoC set up as doxygen_parser, has a python script. It was tested locally as well as through the Gitlab Pipeline
Example: 
```
python3 doxygen_parser.py doxygen_warnings.log
```

## What is the advantage of using LFS?
Git Large File Storage (LFS) is designed to store large files more efficiently in Git repositories. The main advantages of using LFS for a repository, which contains binaries, are:

- Reduced Repository Size: LFS stores large binary files outside the main repository, significantly reducing the size of the repository. This improves performance when cloning or pulling the repository.
- Efficient Versioning of Large Files: Git LFS allows large binary files to be versioned more effectively. Instead of storing the entire binary file in each commit, it stores only a pointer to the file, saving space.
- Faster Cloning: By not storing large files directly in Git, LFS speeds up repository cloning and checkout, especially for users who don't need the large files immediately.

*(Answer taken from online)*

## How to adjust this repository to support LFS?
Firstly we can install git-lfs.
Once done, we can use the `git lfs track *.filetype` to use LFS.

I have read the use of git submodules but in this scenario I believe git-lfs should be good to use?
