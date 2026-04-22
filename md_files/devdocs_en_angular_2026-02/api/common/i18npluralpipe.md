# I18nPluralPipe

I18nPluralPipe



# I18nPluralPipe

Maps a value to a string that pluralizes the value according to locale rules.

[Built-in Pipes](../../guide/templates/pipes#built-in-pipes)

## Pipe usage

```
{{ value_expression | i18nPlural:pluralMap:locale }}
```

## API

```
class I18nPluralPipe implements PipeTransform {
  constructor(_localization: NgLocalization): I18nPluralPipe;
  transform(value: number | null | undefined, pluralMap: { [count: string]: string; }, locale?: string | undefined): string;
}
```

### constructor

`I18nPluralPipe`

@param\_localization`NgLocalization`

@returns`I18nPluralPipe`

### transform

`string`

@paramvalue`number | null | undefined`

the number to be formatted

@parampluralMap`{ [count: string]: string; }`

an object that mimics the ICU format, see <https://unicode-org.github.io/icu/userguide/format_parse/messages/>.

@paramlocale`string | undefined`

a `string` defining the locale to use (uses the current [`LOCALE_ID`](../core/locale_id) by default).

@returns`string`

## Description

Maps a value to a string that pluralizes the value according to locale rules.

---

## Exported by

- `CommonModule`

## Usage Notes

### Example

```
@Component({
  selector: 'i18n-plural-pipe',
  imports: [I18nPluralPipe],
  template: `<div>{{ messages.length | i18nPlural: messageMapping }}</div>`,
})
export class I18nPluralPipeComponent {
  messages: any[] = ['Message 1'];
  messageMapping: {[k: string]: string} = {
    '=0': 'No messages.',
    '=1': 'One message.',
    'other': '# messages.',
  };
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/I18nPluralPipe>
