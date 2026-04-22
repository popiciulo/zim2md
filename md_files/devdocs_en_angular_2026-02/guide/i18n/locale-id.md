# Refer to locales by ID

Refer to locales by ID



# Refer to locales by ID

  

Angular uses the Unicode *locale identifier* (Unicode locale ID) to find the correct locale data for internationalization of text strings.

### Unicode locale ID

- A locale ID conforms to the [Unicode Common Locale Data Repository (CLDR) core specification](https://cldr.unicode.org/index/cldr-spec "Core Specification | Unicode CLDR Project"). For more information about locale IDs, see [Unicode Language and Locale Identifiers][UnicodeCldrDevelopmentCoreSpecificationLocaleIDs].
- CLDR and Angular use [BCP 47 tags](https://www.rfc-editor.org/info/bcp47 "BCP 47 | RFC Editor") as the base for the locale ID

A locale ID specifies the language, country, and an optional code for further variants or subdivisions. A locale ID consists of the language identifier, a hyphen (`-`) character, and the locale extension.

```
{language_id}-{locale_extension}
```

**HELPFUL:** To accurately translate your Angular project, you must decide which languages and locales you are targeting for internationalization.

Many countries share the same language, but differ in usage. The differences include grammar, punctuation, formats for currency, decimal numbers, dates, and so on.

For the examples in this guide, use the following languages and locales.

| Language | Locale | Unicode locale ID |
| --- | --- | --- |
| English | Canada | `en-CA` |
| English | United States of America | `en-US` |
| French | Canada | `fr-CA` |
| French | France | `fr-FR` |

The [Angular repository](https://github.com/angular/angular/tree/main/packages/common/locales "angular/packages/common/locales | angular/angular | GitHub") includes common locales.

For a list of language codes, see [ISO 639-2](https://www.loc.gov/standards/iso639-2).

## Set the source locale ID

Use the Angular CLI to set the source language in which you are writing the component template and code.

By default, Angular uses `en-US` as the source locale of your project.

To change the source locale of your project for the build, complete the following actions.

1. Open the [`angular.json`](https://angular.dev/reference/configs/workspace-config "Angular workspace configuration | Angular") workspace build configuration file.
2. Add or modify the `sourceLocale` field inside the `i18n` section:

```
{
  "projects": {
    "your-project": {
      "i18n": {
        "sourceLocale": "ca"  // Use your desired locale code
      }
    }
  }
}
```

## What's next

  [Format data based on locale](format-data-locale)  

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/i18n/locale-id>
