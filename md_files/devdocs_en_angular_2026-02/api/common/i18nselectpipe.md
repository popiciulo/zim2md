# I18nSelectPipe

I18nSelectPipe



# I18nSelectPipe

Generic selector that displays the string that matches the current value.

[Built-in Pipes](../../guide/templates/pipes#built-in-pipes)

## Pipe usage

```
{{ value_expression | i18nSelect:mapping }}
```

## API

```
class I18nSelectPipe implements PipeTransform {
  transform(value: string | null | undefined, mapping: { [key: string]: string; }): string;
}
```

### transform

`string`

@paramvalue`string | null | undefined`

a string to be internationalized.

@parammapping`{ [key: string]: string; }`

an object that indicates the text that should be displayed for different values of the provided `value`.

@returns`string`

## Description

Generic selector that displays the string that matches the current value.

If none of the keys of the `mapping` match the `value`, then the content of the `other` key is returned when present, otherwise an empty string is returned.

---

## Exported by

- `CommonModule`

## Usage Notes

### Example

```
@Component({
  selector: 'i18n-select-pipe',
  imports: [I18nSelectPipe],
  template: `<div>{{ gender | i18nSelect: inviteMap }}</div>`,
})
export class I18nSelectPipeComponent {
  gender: string = 'male';
  inviteMap: any = {'male': 'Invite him.', 'female': 'Invite her.', 'other': 'Invite them.'};
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/I18nSelectPipe>
