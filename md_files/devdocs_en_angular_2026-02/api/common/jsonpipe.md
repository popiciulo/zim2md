# JsonPipe

JsonPipe



# JsonPipe

Converts a value into its JSON-format representation. Useful for debugging.

[Built-in Pipes](../../guide/templates/pipes#built-in-pipes)

## Pipe usage

```
{{ value_expression | json }}
```

## API

```
class JsonPipe implements PipeTransform {
  transform(value: any): string;
}
```

### transform

`string`

@paramvalue`any`

A value of any type to convert into a JSON-format string.

@returns`string`

## Description

Converts a value into its JSON-format representation. Useful for debugging.

---

## Exported by

- `CommonModule`

## Usage Notes

The following component uses a JSON pipe to convert an object to JSON format, and displays the string in both formats for comparison.

```
@Component({
  selector: 'json-pipe',
  imports: [JsonPipe],
  template: `<div>
    <p>Without JSON pipe:</p>
    <pre>{{ object }}</pre>
    <p>With JSON pipe:</p>
    <pre>{{ object | json }}</pre>
  </div>`,
})
export class JsonPipeComponent {
  object: Object = {foo: 'bar', baz: 'qux', nested: {xyz: 3, numbers: [1, 2, 3, 4, 5]}};
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/JsonPipe>
