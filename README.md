# UTS 32555 University Application

This application serves as a coding assessment for the 32555 course at UTS, providing both a command-line interface (CLI) and a graphical user interface (GUI) for university subject enrollment.

## Features

- **CLI Mode**: Engage with the application using command-line commands.
- **GUI Mode**: User-friendly interface for easy navigation and task completion.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

1. **Operating Systems:** The application is compatible with both Windows and Mac. It has been extensively tested on these platforms.
2. **Python Version:** The application is written using Python 3.11.5. It should run on Python versions 3.x.
3. **Dependencies:** The application relies on third-party libraries. Ensure you have the following packages installed:

   - `customtkinter`
   - `CTkTable`
   - `PIL`

   Use the following commands to install these packages:

   ```bash
   pip3 install customtkinter
   pip3 install CTkTable
   pip3 install Pillow  # PIL is available as Pillow in PyPI

### Installation

To set up the `UTS 32555 University Application`, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine:
   ```bash
   git clone https://github.com/john8862/StudentEnrollmentUTS.git
   ```

2. **Navigate to the Directory**:
   ```bash
   cd StudentEnrollmentUTS
   ```

3. **For GUI**: 
   The primary GUI version is located under the `GUI` folder. To run this GUI version, navigate to the `GUI` folder and run the starting file:
   ```bash
   cd GUI
   python3 SignInNew.py
   ```

4. **For CLI**:
   The CLI version is located in the root directory of the repository. To run the CLI version, simply execute:
   ```bash
   python3 CLI.py
   ```

5. **Database**:
   The application uses a database file named `student.data` that should be present in the root directory.

6. **Archived GUI Version**:
   There's another GUI version that has been archived and is located in the `EOL` folder. This version will no longer receive support or updates. You can still access and review it, but it's recommended to use the primary GUI for regular use.

## Usage

The `UTS 32555 University Application` provides interfaces for both students and admins to manage student enrollment processes. All student information, including registrations and subject enrollments, is stored in the `student.data` file.

### Data Storage:
All student information, from both CLI and GUI interfaces, is saved directly to the `student.data` file. Any changes to registrations or subject enrollments made through the interfaces will reflect in this file.

### CLI:
The CLI interface caters to both students and admins:

- **Student Session**:
  1. Accessible through both login and registration options.
  2. Enables students to manage their enrollment details.

- **Admin Session**:
  1. No login or account setup required; admins have direct access.
  2. Provides admins with tools to manage overall student enrollments and other administrative tasks.

### GUI:
The GUI is tailored for students and offers the following features:

- **Login**: Existing students can sign in to manage their details.
- **Registration**: New students can register and create their accounts.
- **Change Password**: Students can securely change their account passwords.
- **Enrollment**: Enrollment changes are saved automatically. If a student enrolls in a new subject or drops an existing one, the changes are instantly saved to `student.data`.

**Note**: Direct modifications to the `student.data` file outside of the provided interfaces are not recommended as they might lead to data inconsistencies or errors in the application.

## Screenshots

> Placeholder for screenshots. Screenshots of the application in action will be added here soon.

- ![Description of Screenshot 1](URL-of-Screenshot-1)
- ![Description of Screenshot 2](URL-of-Screenshot-2)
- ![Description of Screenshot 3](URL-of-Screenshot-3)

## FAQ

**Q: How do I reset my student password in the GUI?**
A: Use the "Change Password" feature in the GUI or CLI menu after login is the intended way. But if the user wants to test data, the password can be changed in `student.data` under a certain user. It's not a recommended way because it may break the password validation rule and create errors.

**Q: Can I use this application offline?**
A: Yes, the application works offline. All data is stored locally in `student.data`.

**Q: Is there any backup feature for the student data?**
A: Currently, there is no backup feature for this application.

**Q: Are there any plans to support other platforms besides Windows and Mac?**
A: Other platforms were not tested. Users can test by themselves. As it's using customtkinter, the appearance should be the same. However, the cursor setup is not included which may cause errors.

**Q: I encountered an error while enrolling for a subject. What should I do?**
A: Raise an issue on GitHub. The author may check and solve it if time allows.

**Q: Is my data encrypted and secure?**
A: No security feature is designed in this program. Users can develop it further if they wish.

**Q: How often is this application updated?**
A: This development is for subject assessment. The update frequency is uncertain. However, a changelog will be published once there is an update.

## Support

For support, users are encouraged to raise an issue in the [GitHub repository](https://github.com/john8862/StudentEnrollmentUTS.git). The authors will review and address it when time permits, but there's no guaranteed SLA (Service Level Agreement).

## Acknowledgements

### Libraries and Modules

The development of this application benefited from several external libraries and built-in Python modules. For third-party libraries, the following were employed:

- [customtkinter](https://pypi.org/project/customtkinter/)
- [CTkTable](https://pypi.org/project/CTkTable/)
- [PIL (Pillow)](https://pypi.org/project/Pillow/)

### Design Inspiration

1. The newer version of the GUI was heavily inspired by [this library](https://github.com/RoyChng/customtkinter-examples). Not only the layout but some of the picture assets were also utilized in my code and design. This library was discovered through [this video](https://www.youtube.com/watch?v=Miydkti_QVE).

2. Certain design methodologies were gleaned from [this tutorial video](https://www.youtube.com/watch?v=mop6g-c5HEY&t=34526s).

3. The introduction and eventual use of `customtkinter` came after watching [this instructional video](https://www.youtube.com/watch?v=MvzK9Oguxcg&t=1s).

4. The design of the older version of the GUI took inspiration from [this YouTube channel](https://www.youtube.com/@codinglifestyle4u).

### Team Members and Collaborators

Special thanks to [@ink-commits](https://github.com/ink-commits) for being an integral team member and for their efforts in completing the first version of this program.

## Contributing

We welcome contributions from the community! Whether it's fixing bugs, adding new features, or updating documentation, your efforts are appreciated.

### How to Contribute:

1. **Fork the Repository:** Start by forking [this repository](https://github.com/john8862/StudentEnrollmentUTS.git) to your own GitHub account.

2. **Clone the Forked Repository:** 
   ```bash
   git clone https://github.com/your-username/StudentEnrollmentUTS.git
   ```

3. **Create a New Branch:** Before making changes, create a new branch. This will make it easier to handle the different features or fixes you're working on.
   ```bash
   git checkout -b "name-of-your-branch"
   ```

4. **Make Your Changes:** Implement your changes, additions, or fixes.

5. **Commit and Push:** Once done, commit your changes and push them to your fork.
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin name-of-your-branch
   ```

6. **Open a Pull Request:** Go to the GitHub page of your forked repository and click on "New Pull Request." Make sure to provide a detailed description of your changes.

Please ensure your code follows the existing style conventions of the project. Before submitting a PR, also make sure to test your changes thoroughly.

### Reporting Bugs or Issues:

If you find any bugs or issues, please report them by opening an issue on the [GitHub issues page](https://github.com/john8862/StudentEnrollmentUTS/issues).

## Contributing

We welcome contributions from the community! Whether it's fixing bugs, adding new features, or updating documentation, your efforts are appreciated.

### How to Contribute:

1. **Fork the Repository:** Start by forking [this repository](https://github.com/john8862/StudentEnrollmentUTS.git) to your own GitHub account.
   
2. **Clone the Forked Repository:** 
   ```bash
   git clone https://github.com/your-username/StudentEnrollmentUTS.git
   ```

3. **Create a New Branch:** Before making changes, create a new branch according to the naming conventions:
   - For features: `feature/{featureName}`
   - For hotfixes: `hotfix/{hotfixName}`
   ```bash
   git checkout -b name-of-your-branch
   ```

4. **Make Your Changes:** Implement your changes, additions, or fixes.

5. **Commit and Push:** Commit messages should follow the Angular Git Commit Guideline. A single commit should have changes of the same category and should not have more than 3 changes. 
   ```bash
   git add .
   git commit -m "Description of changes following Angular Git Commit Guideline"
   git push origin name-of-your-branch
   ```

6. **Open a Pull Request:** Go to the GitHub page of your forked repository and click on "New Pull Request." Make sure to provide a detailed description of your changes.

Please ensure your code follows the existing style conventions of the project. Before submitting a PR, also make sure to test your changes thoroughly. Any commits that do not follow the mentioned guidelines will not be accepted.

### Reporting Bugs or Issues:

If you find any bugs or issues, please report them by opening an issue on the [GitHub issues page](https://github.com/john8862/StudentEnrollmentUTS/issues).
