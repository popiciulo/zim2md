# NgPluralCase

NgPluralCase



# NgPluralCase

Creates a view that will be added/removed from the parent [`NgPlural`](ngplural) when the given expression matches the plural expression according to CLDR rules.

## API

```
class NgPluralCase {
  constructor(value: string, template: TemplateRef<Object>, viewContainer: ViewContainerRef, ngPlural: NgPlural): NgPluralCase;
  override value: string;
}
```

### constructor

`NgPluralCase`

@paramvalue`string`

@paramtemplate`TemplateRef<Object>`

@paramviewContainer`ViewContainerRef`

@paramngPlural`NgPlural`

@returns`NgPluralCase`

### value

`string`

## Description

Creates a view that will be added/removed from the parent [`NgPlural`](ngplural) when the given expression matches the plural expression according to CLDR rules.

---

## Exported by

- `CommonModule`

## Usage Notes

```
<some-element [ngPlural]="value">
  <ng-template ngPluralCase="=0">...</ng-template>
  <ng-template ngPluralCase="other">...</ng-template>
</some-element>
```

See [`NgPlural`](ngplural) for more details and example.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/NgPluralCase>
