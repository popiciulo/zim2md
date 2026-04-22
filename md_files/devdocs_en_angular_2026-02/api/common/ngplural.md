# NgPlural

NgPlural



# NgPlural

Adds / removes DOM sub-trees based on a numeric value. Tailored for pluralization.

## API

```
class NgPlural {
  constructor(_localization: NgLocalization): NgPlural;
  @Input() set ngPlural(value: number);
  addCase(value: string, switchView: SwitchView): void;
}
```

### constructor

`NgPlural`

@param\_localization`NgLocalization`

@returns`NgPlural`

### ngPlural

`number`

### addCase

`void`

@paramvalue`string`

@paramswitchView`SwitchView`

@returns`void`

## Description

Adds / removes DOM sub-trees based on a numeric value. Tailored for pluralization.

Displays DOM sub-trees that match the switch expression value, or failing that, DOM sub-trees that match the switch expression's pluralization category.

To use this directive you must provide a container element that sets the `[ngPlural]` attribute to a switch expression. Inner elements with a `[ngPluralCase]` will display based on their expression:

- if `[ngPluralCase]` is set to a value starting with `=`, it will only display if the value matches the switch expression exactly,
- otherwise, the view will be treated as a "category match", and will only display if exact value matches aren't found and the value maps to its category for the defined locale.

See <http://cldr.unicode.org/index/cldr-spec/plural-rules>

---

## Exported by

- `CommonModule`

## Usage Notes

```
<some-element [ngPlural]="value">
  <ng-template ngPluralCase="=0">there is nothing</ng-template>
  <ng-template ngPluralCase="=1">there is one</ng-template>
  <ng-template ngPluralCase="few">there are a few</ng-template>
</some-element>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/NgPlural>
