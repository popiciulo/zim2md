# UrlSegmentGroup

UrlSegmentGroup



# UrlSegmentGroup

Represents the parsed URL segment group.

## API

```
class UrlSegmentGroup {
  constructor(segments: UrlSegment[], children: { [key: string]: UrlSegmentGroup; }): UrlSegmentGroup;
  parent: UrlSegmentGroup | null;
  override segments: UrlSegment[];
  override children: { [key: string]: UrlSegmentGroup; };
  hasChildren(): boolean;
  readonly numberOfChildren: number;
  toString(): string;
}
```

### constructor

`UrlSegmentGroup`

@paramsegments`UrlSegment[]`

The URL segments of this group. See [`UrlSegment`](urlsegment) for more information

@paramchildren`{ [key: string]: UrlSegmentGroup; }`

The list of children of this group

@returns`UrlSegmentGroup`

### parent

`UrlSegmentGroup | null`

The parent node in the url tree

### segments

`UrlSegment[]`

The URL segments of this group. See [`UrlSegment`](urlsegment) for more information

### children

`{ [key: string]: UrlSegmentGroup; }`

The list of children of this group

### hasChildren

`boolean`

Whether the segment has child segments

@returns`boolean`

### numberOfChildren

`number`

Number of child segments

### toString

`string`

@returns`string`

## Description

Represents the parsed URL segment group.

See [`UrlTree`](urltree) for more information.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/UrlSegmentGroup>
