# MissingTranslationStrategy

MissingTranslationStrategy



# MissingTranslationStrategy

Use this enum at bootstrap as an option of `bootstrapModule` to define the strategy that the compiler should use in case of missing translations:

- Error: throw if you have missing translations.
- Warning (default): show a warning in the console and/or shell.
- Ignore: do nothing.

## API

```
enum MissingTranslationStrategy {
  Error: MissingTranslationStrategy.Error;
  Warning: MissingTranslationStrategy.Warning;
  Ignore: MissingTranslationStrategy.Ignore;
}
```

### Error

### Warning

### Ignore

## Description

Use this enum at bootstrap as an option of `bootstrapModule` to define the strategy that the compiler should use in case of missing translations:

- Error: throw if you have missing translations.
- Warning (default): show a warning in the console and/or shell.
- Ignore: do nothing.

See the [i18n guide](../../guide/i18n/merge#report-missing-translations) for more information.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/MissingTranslationStrategy>
