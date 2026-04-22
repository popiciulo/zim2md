# Attribute

Attribute



# Attribute

Parameter decorator for a directive constructor that designates a host-element attribute whose value is injected as a constant string literal.

## API

```
@Attribute(name: string);
```

## Usage Notes

Suppose we have an `<input>` element and want to know its `type`.

```
<input type="text">
```

The following example uses the decorator to inject the string literal `text` in a directive.

```
@Directive({
  selector: 'input',
})
class InputAttrDirective {
  constructor(@Attribute('type') type: string) {
    // type would be 'text' in this example
  }
}
```

The following example uses the decorator in a component constructor.

```
@Component({
  selector: 'page',
  template: 'Title: {{title}}',
})
class Page {
  title: string;
  constructor(@Attribute('title') title: string) {
    this.title = title;
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/Attribute>
