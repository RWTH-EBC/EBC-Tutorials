# Table of Contents
1. [Introduction](#introduction)
1. [Motivation: Why version control?](#motivation-why-version-control)
1. [Understanding the concept](#understanding-the-concept)
    1. [The repository](#the-repository)
    1. [The big picture](#the-big-picture)
1. [Different servers](#different-servers)
1. [Installing Git](#installing-git)
1. [A simple Git example](#a-simple-git-example)
    1. [Creating a new project on the server](#creating-a-new-project-on-the-server)
    1. [Cloning the repo to our local machine](#cloning-the-repo-to-our-local-machine)
    1. [Commiting a text file to the repo](#commiting-a-text-file-to-the-repo)
        1. [Creating example1.txt](#creating-example1txt)
        1. [Checking the current status of working copy and repo](#checking-the-current-status-of-working-copy-and-repo)
        1. [Adding the text file to the stage](#adding-the-text-file-to-the-stage)
        1. [Committing the file](#committing-the-file)
    1. [Pushing our changes from the local repo to the server](#pushing-our-changes-from-the-local-repo-to-the-server)
    1. [Working with the issue tracker](#working-with-the-issue-tracker)
    1. [Creating a new branch and commiting changes](#creating-a-new-branch-and-commiting-changes)
    1. [Merging a branch back into the master](#merging-a-branch-back-into-the-master)
        1. [Merge Requests / Pull Requests](#merge-requests--pull-requests)
        1. [Pull changes from the server to the local repo](#pull-changes-from-the-server-to-the-local-repo)
1. [What next?](#what-next)

# Introduction

This tutorial aims at helping you to get started with version control using Git from an EBC-perspective. If you have suggestions on how to improve this tutorial, please make sure to bring this to our attention using the [issue tracker](https://github.com/RWTH-EBC/EBC-Tutorials/issues). Don't be shy about this, if something does not become clear in this tutorial, it is likely not your fault, but a usability bug of this tutorial, so the issue tracker is a good place to talk about it.

The intended audience of this tutorial are students with no prior experience in version control systems, but we hope that it is also helpful for every interested reader.

[Go back :arrow_up:](#table-of-contents)
# Motivation: Why version control?

There are many good reasons for using version control and we couldn't agree more with Michael Tiller's [What Engineers Need to Know About Version Control](http://blog.xogeny.com/blog/version-control/). We encourage you to take a minute and read that blog post. (Also, we like the image he uses to illustrate the dangers of not using version control.) In case you feel like [tl;dr](https://en.wikipedia.org/wiki/Wikipedia:Too_long;_didn't_read) (which you shouldn't) here is quick summary of the main arguments for using version control:

* **Danger**: You can lose work by computer crashes or accidentally deleting/not saving. Version control helps to prevent that.
* **History**: Especially when writing a thesis or developing code (e.g. in Modelica or Python), many people make safety copies along the way, resulting in file names like `thesis_2016-06-17_v4_corrected_final.docx` (often followed by `thesis_2016-06-17_v4_corrected_final2.docx`...)  or  `HeatingSystem_test-4_-new-control_valid.mo`. Version control helps to prevent that.
* **Collaboration**: When working with others, we often waste time exchanging and adapting different versions of files. Version control provides a strong platform to manage collaboration better.

We hope these reasons are motivation enough to read on and learn how version control can help us to improve our workflows.

[Go back :arrow_up:](#table-of-contents)
# Understanding the concept

Unfortunately, before getting our hands on an example that demonstrates how to use Git for our version control we need to understand the concept of Git's version control system and introduce a few terms in order to make sure we speak the same language when talking about Git.

[Go back :arrow_up:](#table-of-contents)
## The repository

If your computer is running a Windows system, you are used to files being displayed in the explorer. For a local copy of **AixLib**, this may look something like this:

![File system screenshot](https://cloud.githubusercontent.com/assets/5516900/16150660/b4608894-3498-11e6-9ac7-442ab3c4fb1a.png)

Let's imagine all these files at a specific moment in time (a "snapshot" of the entire file system within a given parent directory) to be represented by a blue dot that looks like this:

![A blue dot representing the a snapshot of the file system](https://cloud.githubusercontent.com/assets/5516900/16150744/413e13d0-3499-11e6-9eac-e0e38728b66e.png)

What a version control system like Git does is that it allows us to save, organize and manage many of such snapshots within a *repository*. We may visualize the concept of such a *repository* (or *repo* in short) like this:

![Concept drawing of the repository](https://cloud.githubusercontent.com/assets/5516900/16150788/a09a27ec-3499-11e6-9549-4a4db6a57518.png)

Instead of just making changes (intentional or accidental) on the one version of the files that the explorer view offers us and hoping for the best, a version-controlled *repo* enables (and encourages) us to save such snapshots, giving us a timeline of changes that we can inspect and go back in, if we want to undo some changes. In addition, we can organize many of such timelines in parallel, allowing us to work in parallel with our colleagues or try out things with the confidence of knowing that we can always go back to a stable version saved in another snapshot. In Git, each of these parallel "timelines" is called a *branch*. A "snapshot" is called a *commit*. By default, there is one *master* branch. In projects like *AixLib*, we try to always have a stable version of our code on the *master*. Thus, all development and experiments are done in parallel branches (e.g. `New feature 1` and `Wild test 17b` in the figure above). We can have a practically unlimited number of such branches in parallel, create new ones and delete others. In any case, we can always switch between branches, start new ones off our currently selected *commit* and *merge* our developments from one branch back into another (indicated by a green dot in the figure above). We will see how this works in a short time.

[Go back :arrow_up:](#table-of-contents)
## The big picture

You can use Git for version control on your local machine to better manage your files helping with the **History** issue mentioned above, but in order to also address the **Danger** of losing your work locally and to work in **Collaboration** with others, we will need to exchange data with a server. Let's use a similar visualization as introduced above to illustrate this concept:

![05_serverr_stage](https://cloud.githubusercontent.com/assets/5516900/16151700/bc2d3b20-349e-11e6-8c81-e44f4b1706e8.png)

Git is a distributed version control system. This means that your local computer as well as the server and any other computers working on a given project will have a full copy of the repo on their systems. If you are used to working with SVN (another version control system, but a centralized one), this is a notable difference. In Git, you can start new branches, save your commits and checkout alternative versions all locally without being connected to the server. This is great e.g. for working on a train without Wi-Fi, but we will have to keep in mind to actively synchronize our work with the server. We will get to this.

In addition to the repositories on your local computer and on the server, the figure above shows a part called "working copy". We will use this term to refer to what you are actually seeing in your Windows explorer like we showed in the first figure of this document. You will notice any Git repositories in your file system by a folder named `.git` in the top-level directory of the repo (you may have to tell Windows to show you hidden folders for this). When you checkout different branches from your local repo, the working copy will appear to "magically" change to the version that was last committed into this branch. It is absolutely important to understand how the working copy and the repository interact. Please note:
* If you make changes to your local files in your working copy, neither the repo on your local machine nor the one on the server are directly affected by this.
* Changes in your working copy have to be actively committed into your local repository.
* Changes in the working copy can be undone and any commit from the repo can be retrieved into the working copy.

Unfortunately, it will get just one step more complicated before we can start working with Git: We cannot directly commit from our working copy into the local repo. First, we have to *stage* all files we want to include in our commit. We are aware that this may seem unneccessary in the beginning, but you will get used to it and see that it makes sense in order to bundle different changes into different commits to make your history clearer and easier to understand and retrack.

[Go back :arrow_up:](#table-of-contents)
# Different servers

There are several options where the server repository may be hosted. Obviously, there is *GitHub* ([https://github.com/](https://github.com/)). GitHub is probably the most popular service for hosting Git repos. All open-source projects are hosted on GitHub for free, closed-source projects have to be paid. We use GitHub for all our open-source projects like [AixLib](https://github.com/RWTH-EBC/AixLib) and [TEASER](https://github.com/RWTH-EBC/TEASER) (and there's always more to come!).

In addition, RWTH Aachen University runs its own Git Server called RWTH GitLab at [https://git.rwth-aachen.de/](https://git.rwth-aachen.de/). You can log in to RWTH GitLab with your TIM account, making it ideal for starting your own projects (e.g. for your thesis).

Another very important aspect about these Git servers is that they offer a web-view of your repository, integrating an issue tracker, pull requests, network-graphs and much more with your files.

[Go back :arrow_up:](#table-of-contents)
# Installing Git

If you are using your own device, you can simply download and install Git from [https://git-scm.com/](https://git-scm.com/).

If you are using an EBC computer, please install Git using the Software-Center on your Desktop. It is listed as `Software Freedom Conservancy - git`.

Now you are almost ready to use Git for version control. For this tutorial we will use the command line. Yes, we know that some people will prefer a GUI and we will show you how to get started with a GUI at the end of this tutorial, but to understand the concepts and fall back on when the GUI is behaving strangely, we encourage you to bear with us and the command line. In order to make your machine understand Git, you have to add your Git installation (e.g. at `C:\Program Files\Git\bin;)` to the `PATH` environmental variable ("Umgebungsvariable" on a German system):

![06_path](https://cloud.githubusercontent.com/assets/5516900/16152765/9cde5a92-34a3-11e6-8ff0-53feafd4bf23.gif)

[Go back :arrow_up:](#table-of-contents)
# A simple Git example

For this example, we will use the RWTH GitLab Server. The appearance of GitLab
has changed a bit since we created this tutorial, but we hope you will find your
way around nonetheless. If you have no access to that server, any other Git
Server is pretty similar.

[Go back :arrow_up:](#table-of-contents)
## Creating a new project on the server

After logging in to RWTH GitLab at [https://git.rwth-aachen.de/](https://git.rwth-aachen.de/) we can start a new project by clicking on the green button:

![07_new_project](https://cloud.githubusercontent.com/assets/5516900/16153588/3e0957ac-34a7-11e6-9227-8a0d15eb32f2.png)

We can then fill in project name, description (it says optional, but please always provide a description), chose a privacy setting and create the project:

![08_project](https://cloud.githubusercontent.com/assets/5516900/16153753/e9f940b8-34a7-11e6-8fcc-3f4bf93afb04.gif)

At this moment, the repo is empty and exists only on the server. Using the visualization scheme from above, the situation is this:

![09_start](https://cloud.githubusercontent.com/assets/5516900/16153880/9410830e-34a8-11e6-93fa-558667fc5ae1.png)

[Go back :arrow_up:](#table-of-contents)
## Cloning the repo to our local machine

Now we want to start working with this repository. In a limited way, some Git platforms will allow us to modify files
on their web interface, but usually we will want to have the repo locally and work there. Thus, we *clone* the repo to our local machine. To do that, we use the command `git clone <server address of our new repo>` in the command prompt (right-click on the image and chose "show image" for a larger version):

![11_clone](https://cloud.githubusercontent.com/assets/5516900/16154153/e0477fb0-34a9-11e6-8280-e3e211c024fe.gif)

We do get a warning that we seem to have cloned an empty repository, but as this is what we expected, we will not worry about that. Instead, let's go back to the concept view to see what happened:

![10_clone](https://cloud.githubusercontent.com/assets/5516900/16154278/632f4250-34aa-11e6-85ae-62b3765f3121.png)

With `git clone https://...` we created a local repository that is linked to the server repo by the address we gave with the command. Now, the repo exists twice, on the server, and on our local machine. Also, the working copy that we can see in the Windows file system shows us the empty repo. we see a directory that is empty except for the `.git` folder, that indicates that this directory is in fact a git repo:

![12_files](https://cloud.githubusercontent.com/assets/5516900/16154403/f3d9c438-34aa-11e6-8fea-d85c2d0e5f3a.png)

[Go back :arrow_up:](#table-of-contents)
## Commiting a text file to the repo

### Creating example1.txt

Now we can start to demonstrate a few Git features and workflows. First we'll add an empty text file to the working copy (The green symbol on the newly created text file is added by Tortoise Git, a GUI that we will talk about in a short while. Please ignore the symbol for now):

![13_newfile](https://cloud.githubusercontent.com/assets/5516900/16154534/a136e660-34ab-11e6-89e5-7aca9feb1a42.gif)

Remember that this change until now only affects the working copy. The repo has noticed the change, but has not yet done anything to save or manage our new file within its history.

### Checking the current status of working copy and repo

We can use `git status` to get some information about the current state of our working copy and the repo:

![15_status](https://cloud.githubusercontent.com/assets/5516900/16154859/fd048118-34ac-11e6-996e-6bbdf32c416f.gif)

As a response, git tells us that we are on branch `master`, that there are untracked files (`example1.txt`) and that nothing is currently added to commit, meaning that the stage is currently empty.

### Adding the text file to the stage

Before we can commit the file into the repo, first we will thus have to add it to the stage. On a concept level, we are trying to do this:

![14_add](https://cloud.githubusercontent.com/assets/5516900/16154906/3c7c4dda-34ad-11e6-817e-5e68d3e09927.png)

To add the file to the stage, we use the command `git add example1.txt`. After checking again with `git status`, we see that the file is now staged for commit.

![16_add](https://cloud.githubusercontent.com/assets/5516900/16154950/6fe3978c-34ad-11e6-9608-079e05d05fea.gif)

### Committing the file

Now, finally, we are ready to commit the file to our local repo. Again, this is what we are trying to do:

![15_commit](https://cloud.githubusercontent.com/assets/5516900/16155069/f5faed5c-34ad-11e6-9351-010141427da9.png)

Before we actually commit the file to the repo, let's take a second to reflect on what this will do. We will save a snapshot into the history of our project. For this example project, the requirements may not be too strict, but let's have a look into a larger project like **AixLib**. You can see the history of all commits made to the `master` branch at [https://github.com/RWTH-EBC/AixLib/commits/master](https://github.com/RWTH-EBC/AixLib/commits/master). You can browse through all code changes and retrack the history of each individual file. This may be necessary, when trying to determine when and why a change was made that later turned out to cause unwanted side effects. For this, the history built by our commits is a crucial tool. With this in mind, you can see that there are two important aspects for commits:

* A good commit message
* Keeping your commits small, comprehensible and well-structured.

You have to write the commit message for your commit manually. Please write this message in the most useful way for your collaborators and your future self you can come up with. Also, it helps a great deal if you structure your commits in small units. Making many changes to your code today? Make a commit for each task separately rather than one large commit before leaving work and it will be much easier to retrack the history for you and others.

Agreed? Ok, then let's do our first commit. To do this, we have at least two options. First, let's do the faster one. Committing in general is done by using `git commit`. We can directly add the commit message with the `-m modifier`. For example, we can now type `git commit -m "<My commit message>"` (e.g. `git commit -m "Add an empty example text file"`). Like so:

![17_commit](https://cloud.githubusercontent.com/assets/5516900/16155747/24e915fa-34b1-11e6-998b-ec5e118499e5.gif)

[Go back :arrow_up:](#table-of-contents)
## Pushing our changes from the local repo to the server

So far, we have made a first commit to our local repo. If you have also done these steps on your own, you can see that your repo on the server is still empty. In order to get the two repos back in synch, we will send our local changes to the server repo. In Git-lingo, this is called to *push* the local changes to the server. The corresponding git command is `git push`. But in order to tell our local Git repo, which server and branch to push to, we have to add two more keywords to `git push`. The first can be interpreted as the "address" where to send our package of data. Such a connection is called a *remote*. When cloning from a server, Git automatically sets a remote with the name `origin` to the server. You can add many more remotes and juggle your data with multiple server repos, but we will not cover that here. Instead, we are satisfied to push to the server's `master` branch by using `git push origin master` for the moment. Here is our concept view of this step:

![18_push](https://cloud.githubusercontent.com/assets/5516900/16155996/4e624c5c-34b2-11e6-91be-cb631d4c5e38.png)

In the console, this will look like this:

![19_push](https://cloud.githubusercontent.com/assets/5516900/16156027/7dd4d270-34b2-11e6-8aab-016ac7dd3219.gif)

As a response, we see that we successfully pushed from our local `master` to the server repo's `master`

Checking back with the server, we see that we were indeed successful:

![20_server](https://cloud.githubusercontent.com/assets/5516900/16156117/e5cf0120-34b2-11e6-938e-abc43e9014cc.png)

[Go back :arrow_up:](#table-of-contents)
## Working with the issue tracker

We already mentioned, that in addition to the repo itself, servers like GitHub and RWTH GitLab offer us additional services. One of the most important such services is the issue tracker. This allows us to define workflows that are better to manage and facilitating collaboration as well as quality control. Often, workflows are defined in a project's Wiki. It is not a bad idea to take a minute and have a look at the workflow definitions of [AixLib](https://github.com/RWTH-EBC/AixLib/wiki/Contribute-to-AixLib), [the Annex 60 library](https://github.com/iea-annex60/modelica-annex60/wiki/Workflow-for-code-changes), [BuildingSystems](https://github.com/UdK-VPT/BuildingSystems/wiki/How-To-Bug), or [IDEAS](https://github.com/open-ideas/IDEAS/wiki/Style-Guide-and-GitHub-Good-Practice).

A general idea for working on existing projects (let's assume our example project is by now also quite "existing") is to first create an issue on the project's issue tracker and describe briefly what you intend to do. The issue will automatically be assigned by the system with a number. Now we can create a branch, usually naming it after the issue and its number and start working. In our example, let's create an issue to announce that we will add some text to our empty text file:

![21_issue](https://cloud.githubusercontent.com/assets/5516900/16156476/bec66eae-34b4-11e6-99fd-8d3c054ea52b.gif)

[Go back :arrow_up:](#table-of-contents)
## Creating a new branch and commiting changes

For the next steps, we will assume our example project to be a bit larger than it is. Let's imagine, this is a large open-source project used by people who rely on a stable version in the `master` branch for their work. We have now informed them with our issue #1 that we intend to make changes to the repo. In order to have the stable `master` running while we work hard on issue #1, we will split the development's timeline by creating a new parallel branch. In our case, we will call the new branch `issue1_text`. This is what we will try to do:

![22branch](https://cloud.githubusercontent.com/assets/5516900/16156701/c0e4da9e-34b5-11e6-9c0b-401932399125.png)

We will create and switch our working copy to a new branch by typing `git checkout -b issue1_text`:

![23branch](https://cloud.githubusercontent.com/assets/5516900/16156856/60421656-34b6-11e6-87db-afd9c6348e17.gif)

As a result, our local working copy will look the same in the explorer view, but the repo is now in a parallel branch. That means that no matter what we do in this branch, the empty file in the `master` will be safe and unaffected.

Next, we add some text to the example file:

![24text](https://cloud.githubusercontent.com/assets/5516900/16157052/45e5dbac-34b7-11e6-82bb-0a2dda983de4.gif)

Again, we have to stage the changes before committing. In order to not let this become boring, we use a new command for that `git add .`. This adds all changed files to the stage. But note that it does not stage deleted files. To really add all changes, use `git add --all`. But please be careful with this and do not commit changes you did not do intentionally. This is e.g. important with Modelica files if you work in Dymola. Dymola tends to add white space changes to files you did not explicitly work on. Those changes should not be committed.

![25stage](https://cloud.githubusercontent.com/assets/5516900/16157114/7d9bae5a-34b7-11e6-8eb5-d36a386fff12.gif)

And now, we will use the second way of writing our commit message. If we only run `git commit` without the `-m` modifier, a text editor will open. We can write after pressing e.g. `i` for `insert` mode, exit insert mode by pressing `ESC` and save the changes by typing `:wq` (maybe meaning `write` and `quit`). Have a look:

![26commit](https://cloud.githubusercontent.com/assets/5516900/16157412/bc5c6b38-34b8-11e6-9409-b845c5d04ddd.gif)

The nice thing about this editor, apart from reminding us of earlier computing days, is that it's coloring reminds us to keep the first line of the commit message below 80 characters of length, an empty second line and restarting text add the third line if we want to add more info. This is good style, as it will comply with many server websites and make browsing the history easier. Also, note that we included a reference to issue one by typing `For #1`. This will magically mention the commit in our issue tracker once we have pushed our changes. After pushing with `git push origin issue1_text`

![27push](https://cloud.githubusercontent.com/assets/5516900/16157499/1d1e8b68-34b9-11e6-9e39-de0da35bff92.gif)

Our issue tracker mentions the commit as:

![28_issue](https://cloud.githubusercontent.com/assets/5516900/16157543/4256fda2-34b9-11e6-9ef1-5ef1d0bd2a1f.png)

This is useful to show others following the issue that there is ongoing work here.

[Go back :arrow_up:](#table-of-contents)
## Merging a branch back into the master

Let's assume we are satisfied with our work in branch `issue1_text` and want to make this development available to all users by taking the changes from the branch into the `master`. To combine the developments of two branches and continue with one single common timeline in one single branch is called to *merge* one branch into another branch. In our case, we want to *merge* branch `issue1_text` into the `master` branch. In a good Git workflow we often do not do this directly, but first issue a formal *request* for what we want to do. In projects in which 2 or more people collaborate, this is a good way to have some quality control. The developer of the new features or bug fixes usually issues a request, so that a second person can check the code, make comments, and finally accepts or declines the request. More info on e.g. the workflow of **AixLib** can be found here: [https://github.com/RWTH-EBC/AixLib/wiki/Contribute-to-AixLib](https://github.com/RWTH-EBC/AixLib/wiki/Contribute-to-AixLib).

### Merge Requests / Pull Requests

The *request* we have been referring to is called a *Pull Request* on GitHub and *Merge Request* at GitLab. Apart from the name difference, the procedure is quite the same. The requests can be created on the projects webpage. For **AixLib** on GitHub, you can have a look at the pull requests at [https://github.com/RWTH-EBC/AixLib/pulls](https://github.com/RWTH-EBC/AixLib/pulls). For our example, creating a merge request can look something like this:

![28_merge](https://cloud.githubusercontent.com/assets/5516900/16190132/06590fc6-36de-11e6-87ac-98da523910b9.gif)

As shown above, we click to create a *New Merge Request*. In the next page, we select our *source branch* and the *target branch* we want to merge into. In our case, as mentioned above, we want to *merge* branch `issue1_text` into the `master` branch. Then we give a quick description of what this merge request addressed, including a reference to the issue we have created before to document our intented developments. Finally, we assign one of our colleagues (in this case we assigned Peter) to check our code, give feedback and accept or decline the request.

In this case, Peter accepted the request directly. <del>We can see the merging
of our two branches (and their "timelines") visualized by clicking on *Commits*
in GitLab's left-aligned menu and choosing the *Network* view in the top menu
</del> *Here GitLab has changed its organization of the pages: You can now find
the Network Graph by clicking "Repository" and then navigating to "Graph"*:

![30merge](https://cloud.githubusercontent.com/assets/5516900/16190455/a53905be-36df-11e6-85f8-574d69cb2017.png)

*By now, GitLab will suggest to directly delete the branch on the server repository after merging the branch. You can safely do so. If you also want to delete the branch from your local repository, we'll do that in a second.*

### Pull changes from the server to the local repo

So now we have successfully merged the two branches on our server repo on GitLab. But we have to keep in mind, that this does not directly affect our local repo. The current state in our concept view can be shown like this:

![31_merge](https://cloud.githubusercontent.com/assets/5516900/16190586/6346fcaa-36e0-11e6-9cab-cada02d67c1b.png)

In order to get the changes from the server repo to our local repo, we have to actively ask for them. Above, we *pushed* our local changes to the server repo. In a similar way, we will now *pull* the changes on the server back to our local repo. But calling `git status` again on our local repo reminds us, that our checked out working copy is still on branch `issue1_text` (you can also see this in the drawing above, where the working copy has that branch's background color):

![32_status](https://cloud.githubusercontent.com/assets/5516900/16190923/ea7755e8-36e1-11e6-8fee-3059e60f5ed0.gif)

This local branch is not affected by any changes on the server, even if you deleted the branch `issue1_text` on the server repo. On the server's `master` branch, we merged the changes from branch `issue1_text`. What we actually want now is to *pull* the latest changes from the server's `master` branch into our local `master` branch. To do that, we thus switch back our local working copy to the master branch. We can do this by calling `git checkout master`:

![33_master](https://cloud.githubusercontent.com/assets/5516900/16191065/b9cc9cfe-36e2-11e6-87ea-d8f3d675996a.gif)

Now our local working copy is back on the master, enabling us to pull the server's master.
Do not get confused by git's answer: `your branch is up-to-date with 'origin/master'.`. Your local repository is not aware of the changes you just did on the server repo, so this is a comparison between your working copy (you just checked out) and the local master. To update your repo to the latest information on the server, use `git fetch origin`. If you follow this with a `git status` request, git should report with a new message informing you that your local copy is behind the server's version.

![34_pull](https://cloud.githubusercontent.com/assets/5516900/16191363/23c718e0-36e4-11e6-8747-95524656eaf3.png)

Just like with the `git push` command, we use the name of the `remote` (by default, that is `origin`) and the name of the branch we want to *pull* (in our example: `master`) to construct the *pull command* to be `git pull origin master`. We can think of this command as if it were "Please `git`, `pull` the `master` branch from the remote at `origin` and merge it with the current state of my working copy". In action, this looks like this:

![35 pull](https://cloud.githubusercontent.com/assets/5516900/16191589/4c7e92bc-36e5-11e6-9443-1ce0347b4555.gif)

If you want to delete your local branch now, just type `git branch -d issue1_text`.

Great! Now our local repo is back in synch with the server repo and we successfully worked through a first Git example showing us the basic concepts!

[Go back :arrow_up:](#table-of-contents)
# What next?

We hope this tutorial gave you an idea about how Git works. In any case, **please help us to improve this tutorial and make a suggestion for improvement by creating an issue on our [issue tracker](https://github.com/RWTH-EBC/EBC-Tutorials/issues)**! We are convinced that you noticed at least one thing about the tutorial that we can improve on.

If you want to have a look at other tutorials, we can recommend these links:


* [Set Up Git - (GitHub help page)](https://help.github.com/articles/set-up-git/)
* [Git tutorial by Roger Dudler](http://rogerdudler.github.io/git-guide/)
* [Git cheat sheet (useful commands)](http://rogerdudler.github.io/git-guide/files/git_cheat_sheet.pdf)
* [Git tutorial by atlassian ](https://www.atlassian.com/git)

And finally, we promised you an alternative to the command line interface. Here is the link to a video tutorial to Tortoise GIT:

* [Video tutorial for using Git with Tortoise Git](https://www.youtube.com/watch?v=fNPLuJTTto0 )

[Go back :arrow_up:](#table-of-contents)
