
# github-org-stats  
  
Automatically scan your GitHub organizational repositories and generate a language usage summary based on your contributions.    
  
---  
  
## Features  
  
- Detect all GitHub organizations you belong to  
- Identify repos where you’ve made commits  
- Analyze programming languages used in those repos  
- Export results as a clean Markdown table  
  
---  
  
### Configure environment variables  
  
Create a `.env` file in the project root directory with the following content:  
  
```  
GITHUB_TOKEN=your_personal_access_token  
USERNAME=your_github_username  
```  
  
#### `GITHUB_TOKEN`  
  
- Must be a [Personal Access Token](https://github.com/settings/tokens) with at least the `repo` scope.  
      
- If you're part of an organization with SAML enforcement, make sure the token is **authorized** for that organization.  
      
  
####  `USERNAME`  
  
- Your GitHub username. This is used to filter commits made by you in organization repositories.  
  
## 📄 Sample Output  
  
### 💻 My Contributions (Across Organizations)  
  
_Last scan: **2025-04-14 12:53:33 AEST**_  
  
| Language | Bytes |  
|----------|--------|  
| C | 9,276,345 |  
| C# | 432,978 |  
| TypeScript | 184,532 |  
| Objective-C++ | 100,908 |  
| ShaderLab | 80,492 |  
| HTML | 21,997 |  
| Python | 20,895 |  
| Mathematica | 15,479 |  
| HLSL | 13,994 |  
| JavaScript | 3,712 |  
| Makefile | 1,640 |  
| CSS | 59 |  
  
_Powered by [github-org-stats](https://github.com/TheHQ98/github-org-stats)_  
  
## 📜 License  
  
This project is licensed under the [MIT License](LICENSE).