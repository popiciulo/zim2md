# $localize

$localize



# $localize

Tag a template literal string for localization.

## API

```
const $localize: LocalizeFn;
```

## Description

Tag a template literal string for localization.

For example:

```
$localize `some string to localize`
```

**Providing meaning, description and id**

You can optionally specify one or more of `meaning`, `description` and `id` for a localized string by pre-pending it with a colon delimited block of the form:

```
$localize`:meaning|description@@id:source message text`;

$localize`:meaning|:source message text`;
$localize`:description:source message text`;
$localize`:@@id:source message text`;
```

This format is the same as that used for `i18n` markers in Angular templates. See the [Angular i18n guide](../../../guide/i18n/prepare#mark-text-in-component-template).

**Naming placeholders**

If the template literal string contains expressions, then the expressions will be automatically associated with placeholder names for you.

For example:

```
$localize `Hi ${name}! There are ${items.length} items.`;
```

will generate a message-source of `Hi {$PH}! There are {$PH_1} items`.

The recommended practice is to name the placeholder associated with each expression though.

Do this by providing the placeholder name wrapped in `:` characters directly after the expression. These placeholder names are stripped out of the rendered localized string.

For example, to name the `items.length` expression placeholder `itemCount` you write:

```
$localize `There are ${items.length}:itemCount: items`;
```

**Escaping colon markers**

If you need to use a `:` character directly at the start of a tagged string that has no metadata block, or directly after a substitution expression that has no name you must escape the `:` by preceding it with a backslash:

For example:

```
// message has a metadata block so no need to escape colon
$localize `:some description::this message starts with a colon (:)`;
// no metadata block so the colon must be escaped
$localize `\:this message starts with a colon (:)`;
```

```
// named substitution so no need to escape colon
$localize `${label}:label:: ${}`
// anonymous substitution so colon must be escaped
$localize `${label}\: ${}`
```

**Processing localized strings:**

There are three scenarios:

- **compile-time inlining**: the [`$localize`]($localize) tag is transformed at compile time by a transpiler, removing the tag and replacing the template literal string with a translated literal string from a collection of translations provided to the transpilation tool.
- **run-time evaluation**: the [`$localize`]($localize) tag is a run-time function that replaces and reorders the parts (static strings and expressions) of the template literal string with strings from a collection of translations loaded at run-time.
- **pass-through evaluation**: the [`$localize`]($localize) tag is a run-time function that simply evaluates the original template literal string without applying any translations to the parts. This version is used during development or where there is no need to translate the localized template literals.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/localize/init/$localize>
