# NgClass

NgClass



# NgClass

Adds and removes CSS classes on an HTML element.

[Class bindings](../../guide/templates/binding#css-class-and-style-property-bindings)

## API

```
class NgClass implements DoCheck {
  constructor(_ngEl: ElementRef<any>, _renderer: Renderer2): NgClass;
  @Input('class') set klass(value: string);
  @Input() set ngClass(value: string | string[] | Set<string> | { [klass: string]: any; } | null | undefined);
}
```

### constructor

`NgClass`

@param\_ngEl`ElementRef<any>`

@param\_renderer`Renderer2`

@returns`NgClass`

### klass

`string`

### ngClass

`string | string[] | Set<string> | { [klass: string]: any; } | null | undefined`

### ngDoCheck

`void`

@returns`void`

## Description

Adds and removes CSS classes on an HTML element.

The CSS classes are updated as follows, depending on the type of the expression evaluation:

- `string` - the CSS classes listed in the string (space delimited) are added,
- `Array` - the CSS classes declared as Array elements are added,
- `Object` - keys are CSS classes that get added when the expression given in the value evaluates to a truthy value, otherwise they are removed.

---

## Exported by

- `CommonModule`

## Usage Notes

```
<some-element [ngClass]="stringExp|arrayExp|objExp|Set">...</some-element>

<some-element [ngClass]="{'class1 class2 class3' : true}">...</some-element>
```

For more simple use cases you can use the [class bindings](../../guide/templates/binding#css-class-and-style-property-bindings) directly. It doesn't require importing a directive.

```
<some-element [class]="'first second'">...</some-element>

<some-element [class.expanded]="isExpanded">...</some-element>

<some-element [class]="['first', 'second']">...</some-element>

<some-element [class]="{'first': true, 'second': true, 'third': false}">...</some-element>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/NgClass>
