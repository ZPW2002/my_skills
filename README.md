# my_skills

个人 Agent Skills 合集。每个子目录是一个自包含的 skill 包（`SKILL.md` + 资源文件），
不绑定任何特定工具——复制或软链到支持 skills 目录约定的环境即可启用，例如：

```bash
git clone https://github.com/ZPW2002/my_skills.git
cp -r my_skills/mg-film-prompt ~/.agents/skills/
```

## 收录清单

| Skill | 说明 |
|---|---|
| [`mg-film-prompt/`](mg-film-prompt/) | MG 动效短片：15 种经典风格选型 + 完整制作提示词生成，附机械校验脚本与评审迭代方法。方法论提炼自 [mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15)（MIT） |
