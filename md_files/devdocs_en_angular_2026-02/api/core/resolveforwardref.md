# resolveForwardRef

resolveForwardRef



# resolveForwardRef

Lazily retrieves the reference value from a forwardRef.

[forwardRef](forwardref)

## API

```
function resolveForwardRef<T>(type: T): T;
```

### resolveForwardRef

`T`

Lazily retrieves the reference value from a forwardRef.

Acts as the identity function when given a non-forward-ref value.

@paramtype`T`

@returns`T`

Usage notes

### Example

{@example core/di/ts/forward\_ref/forward\_ref\_spec.ts region='resolve\_forward\_ref'}

## Description

Lazily retrieves the reference value from a forwardRef.

Acts as the identity function when given a non-forward-ref value.

## Usage Notes

### Example

```
const ref = forwardRef(() => 'refValue');
      expect(resolveForwardRef(ref as any)).toEqual('refValue');
      expect(resolveForwardRef('regularValue')).toEqual('regularValue');
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/resolveForwardRef>
