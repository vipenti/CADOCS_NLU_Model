# CADOCS_NLU_Model | CONTRIBUTING

## Commits

For contributing commit messagges must follow the standard of [Conventional Commits](https://www.conventionalcommits.org/).

Part of the following document is taken from https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines

### Commit Message Format

Each commit message consists of a `header`, a `body` and a `footer`. The header has a special format that includes a `type`, a `scope` and a `subject`:

```
<type>(<scope>): <summary>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The **header** is mandatory and the **scope** of the header must be omitted if the change is common among the packages, otherwise it's mandatory.

```
<type>(<scope>): <description>
  │       │             │
  │       │             └─⫸ A brief description of the commit
  │       │
  │       └─⫸ Commit Scope: dataset | ml | service
  │
  └─⫸ Commit Type: build|ci|docs|feat|fix|refactor|impr|style|test
```

#### Description

- use the imperative, present tense: "change" not "changed" nor "changes"
- don't capitalize the first letter
- no dot (.) at the end

#### Type

Must be one of the following:

- build: Changes that affect the build system or external dependencies
- ci: Changes to our CI configuration files and scripts
- docs: Documentation only changes
- feat: A new feature
- fix: A bug fix
- refactor: A code change that neither fixes a bug nor adds a feature
- impr: Improve an existing feature or existing dataset
- style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- test: Adding missing tests or correcting existing tests

### Scope

The scope must be the project section within the change is happening.

Supported scopes:

- `dataset`
- `ml`
- `service`

### Body

The **body** is optional. Just as in the **description**, use the imperative, present tense: "fix" not "fixed" nor "fixes".
The body should extend the content of the description.

### Footer

The footer is optional. The footer should contain the GitHub issue reference that this commit **Closes**.

## Branches

New branches must follow this format for their names: `<type>/<scope>/<description>`

- `type` and `scope` refer to the ones described in the Commits section.
- `description` must be a word representing the changes happening in the branch.
