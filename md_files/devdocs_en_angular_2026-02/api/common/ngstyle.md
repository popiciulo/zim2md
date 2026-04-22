# NgStyle

NgStyle



# NgStyle

An attribute directive that updates styles for the containing HTML element. Sets one or more style properties, specified as colon-separated key-value pairs. The key is a style name, with an optional `.<unit>` suffix (such as 'top.px', 'font-style.em'). The value is an expression to be evaluated. The resulting non-null value, expressed in the given unit, is assigned to the given style property. If the result of evaluation is null, the corresponding style is removed.

[Style bindings](../../guide/templates/binding#css-class-and-style-property-bindings)

## API

```
class NgStyle implements DoCheck {
  constructor(_ngEl: ElementRef<any>, _differs: KeyValueDiffers, _renderer: Renderer2): NgStyle;
  @Input() set ngStyle(value: { [klass: string]: any; } | null | undefined);
}
```

### constructor

`NgStyle`

@param\_ngEl`ElementRef<any>`

@param\_differs`KeyValueDiffers`

@param\_renderer`Renderer2`

@returns`NgStyle`

### ngStyle

`{ [klass: string]: any; } | null | undefined`

### ngDoCheck

`void`

@returns`void`

## Description

An attribute directive that updates styles for the containing HTML element. Sets one or more style properties, specified as colon-separated key-value pairs. The key is a style name, with an optional `.<unit>` suffix (such as 'top.px', 'font-style.em'). The value is an expression to be evaluated. The resulting non-null value, expressed in the given unit, is assigned to the given style property. If the result of evaluation is null, the corresponding style is removed.

---

## Exported by

- `CommonModule`

## Usage Notes

Set the width of the containing element to a pixel value returned by an expression.

```
<some-element [ngStyle]="{'max-width.px': widthExp}">...</some-element>
```

Set a collection of style values using an expression that returns key-value pairs.

```
<some-element [ngStyle]="objExp">...</some-element>
```

For more simple use cases you can use the [style bindings](../../guide/templates/binding#css-class-and-style-property-bindings) directly. It doesn't require importing a directive.

Set the font of the containing element to the result of an expression.

```
<some-element [style]="{'font-style': styleExp}">...</some-element>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/NgStyle>
