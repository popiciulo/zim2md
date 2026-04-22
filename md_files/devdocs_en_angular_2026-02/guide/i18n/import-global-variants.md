# Import global variants of the locale data

Import global variants of the locale data



# Import global variants of the locale data

  

The [Angular CLI](../../cli "CLI Overview and Command Reference | Angular") automatically includes locale data if you run the [`ng build`](../../cli/build "ng build | CLI | Angular") command with the `--localize` option.

```
ng build --localize
```

**HELPFUL:** The initial installation of Angular already contains locale data for English in the United States (`en-US`). The [Angular CLI](../../cli "CLI Overview and Command Reference | Angular") automatically includes the locale data and sets the [`LOCALE_ID`](../../api/core/locale_id) value when you use the `--localize` option with [`ng build`](../../cli/build "ng build | CLI | Angular") command.

The `@angular/common` package on npm contains the locale data files. Global variants of the locale data are available in `@angular/common/locales/global`.

## import example for French

For example, you could import the global variants for French (`fr`) in `main.ts` where you bootstrap the application.

```
import '@angular/common/locales/global/fr';
```

**HELPFUL:** In an `NgModules` application, you would import it in your `app.module`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/i18n/import-global-variants>
