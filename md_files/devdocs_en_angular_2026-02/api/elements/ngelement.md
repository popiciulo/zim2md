# NgElement

NgElement



# NgElement

Implements the functionality needed for a custom element.

## API

```
abstract class NgElement extends HTMLElement {
  protected abstract ngElementStrategy: NgElementStrategy;
  protected ngElementEventsSubscription: any;
  abstract attributeChangedCallback(attrName: string, oldValue: string | null, newValue: string, namespace?: string | undefined): void;
  abstract connectedCallback(): void;
  abstract disconnectedCallback(): void;
  override accessKey: string;
  readonly override accessKeyLabel: string;
  override autocapitalize: string;
  override autocorrect: boolean;
  override dir: string;
  override draggable: boolean;
  override hidden: boolean;
  override inert: boolean;
  override innerText: string;
  override lang: string;
  readonly override offsetHeight: number;
  readonly override offsetLeft: number;
  readonly override offsetParent: Element | null;
  readonly override offsetTop: number;
  readonly override offsetWidth: number;
  override outerText: string;
  override popover: string | null;
  override spellcheck: boolean;
  override title: string;
  override translate: boolean;
  override writingSuggestions: string;
  override attachInternals(): ElementInternals;
  override click(): void;
  override hidePopover(): void;
  override showPopover(): void;
  override togglePopover(options?: boolean | undefined): boolean;
  override addEventListener<K extends keyof HTMLElementEventMap>(type: K, listener: (this: HTMLElement, ev: HTMLElementEventMap[K]) => any, options?: boolean | AddEventListenerOptions | undefined): void;
  override addEventListener(type: string, listener: EventListenerOrEventListenerObject, options?: boolean | AddEventListenerOptions | undefined): void;
  override removeEventListener<K extends keyof HTMLElementEventMap>(type: K, listener: (this: HTMLElement, ev: HTMLElementEventMap[K]) => any, options?: boolean | EventListenerOptions | undefined): void;
  override removeEventListener(type: string, listener: EventListenerOrEventListenerObject, options?: boolean | EventListenerOptions | undefined): void;
  readonly override attributes: NamedNodeMap;
  override get classList(): DOMTokenList;
  override className: string;
  readonly override clientHeight: number;
  readonly override clientLeft: number;
  readonly override clientTop: number;
  readonly override clientWidth: number;
  readonly override currentCSSZoom: number;
  override id: string;
  override innerHTML: string;
  readonly override localName: string;
  readonly override namespaceURI: string | null;
  override onfullscreenchange: ((this: Element, ev: Event) => any) | null;
  override onfullscreenerror: ((this: Element, ev: Event) => any) | null;
  override outerHTML: string;
  readonly override ownerDocument: Document;
  override get part(): DOMTokenList;
  readonly override prefix: string | null;
  readonly override scrollHeight: number;
  override scrollLeft: number;
  override scrollTop: number;
  readonly override scrollWidth: number;
  readonly override shadowRoot: ShadowRoot | null;
  override slot: string;
  readonly override tagName: string;
  override attachShadow(init: ShadowRootInit): ShadowRoot;
  override checkVisibility(options?: CheckVisibilityOptions | undefined): boolean;
  override closest<K extends keyof HTMLElementTagNameMap>(selector: K): HTMLElementTagNameMap[K] | null;
  override closest<K extends keyof SVGElementTagNameMap>(selector: K): SVGElementTagNameMap[K] | null;
  override closest<K extends keyof MathMLElementTagNameMap>(selector: K): MathMLElementTagNameMap[K] | null;
  override closest<E extends Element = Element>(selectors: string): E | null;
  override computedStyleMap(): StylePropertyMapReadOnly;
  override getAttribute(qualifiedName: string): string | null;
  override getAttributeNS(namespace: string | null, localName: string): string | null;
  override getAttributeNames(): string[];
  override getAttributeNode(qualifiedName: string): Attr | null;
  override getAttributeNodeNS(namespace: string | null, localName: string): Attr | null;
  override getBoundingClientRect(): DOMRect;
  override getClientRects(): DOMRectList;
  override getElementsByClassName(classNames: string): HTMLCollectionOf<Element>;
  override getElementsByTagName<K extends keyof HTMLElementTagNameMap>(qualifiedName: K): HTMLCollectionOf<HTMLElementTagNameMap[K]>;
  override getElementsByTagName<K extends keyof SVGElementTagNameMap>(qualifiedName: K): HTMLCollectionOf<SVGElementTagNameMap[K]>;
  override getElementsByTagName<K extends keyof MathMLElementTagNameMap>(qualifiedName: K): HTMLCollectionOf<MathMLElementTagNameMap[K]>;
  override getElementsByTagName<K extends keyof HTMLElementDeprecatedTagNameMap>(qualifiedName: K): HTMLCollectionOf<HTMLElementDeprecatedTagNameMap[K]>;
  override getElementsByTagName(qualifiedName: string): HTMLCollectionOf<Element>;
  override getElementsByTagNameNS(namespaceURI: "http://www.w3.org/1999/xhtml", localName: string): HTMLCollectionOf<HTMLElement>;
  override getElementsByTagNameNS(namespaceURI: "http://www.w3.org/2000/svg", localName: string): HTMLCollectionOf<SVGElement>;
  override getElementsByTagNameNS(namespaceURI: "http://www.w3.org/1998/Math/MathML", localName: string): HTMLCollectionOf<MathMLElement>;
  override getElementsByTagNameNS(namespace: string | null, localName: string): HTMLCollectionOf<Element>;
  override getHTML(options?: GetHTMLOptions | undefined): string;
  override hasAttribute(qualifiedName: string): boolean;
  override hasAttributeNS(namespace: string | null, localName: string): boolean;
  override hasAttributes(): boolean;
  override hasPointerCapture(pointerId: number): boolean;
  override insertAdjacentElement(where: InsertPosition, element: Element): Element | null;
  override insertAdjacentHTML(position: InsertPosition, string: string): void;
  override insertAdjacentText(where: InsertPosition, data: string): void;
  override matches(selectors: string): boolean;
  override releasePointerCapture(pointerId: number): void;
  override removeAttribute(qualifiedName: string): void;
  override removeAttributeNS(namespace: string | null, localName: string): void;
  override removeAttributeNode(attr: Attr): Attr;
  override requestFullscreen(options?: FullscreenOptions | undefined): Promise<void>;
  override requestPointerLock(options?: PointerLockOptions | undefined): Promise<void>;
  override scroll(options?: ScrollToOptions | undefined): void;
  override scroll(x: number, y: number): void;
  override scrollBy(options?: ScrollToOptions | undefined): void;
  override scrollBy(x: number, y: number): void;
  override scrollIntoView(arg?: boolean | ScrollIntoViewOptions | undefined): void;
  override scrollTo(options?: ScrollToOptions | undefined): void;
  override scrollTo(x: number, y: number): void;
  override setAttribute(qualifiedName: string, value: string): void;
  override setAttributeNS(namespace: string | null, qualifiedName: string, value: string): void;
  override setAttributeNode(attr: Attr): Attr | null;
  override setAttributeNodeNS(attr: Attr): Attr | null;
  override setHTMLUnsafe(html: string): void;
  override setPointerCapture(pointerId: number): void;
  override toggleAttribute(qualifiedName: string, force?: boolean | undefined): boolean;
  override webkitMatchesSelector(selectors: string): boolean;
  override get textContent(): string;
  readonly override baseURI: string;
  readonly override childNodes: NodeListOf<ChildNode>;
  readonly override firstChild: ChildNode | null;
  readonly override isConnected: boolean;
  readonly override lastChild: ChildNode | null;
  readonly override nextSibling: ChildNode | null;
  readonly override nodeName: string;
  readonly override nodeType: number;
  override nodeValue: string | null;
  readonly override parentElement: HTMLElement | null;
  readonly override parentNode: ParentNode | null;
  readonly override previousSibling: ChildNode | null;
  override appendChild<T extends Node>(node: T): T;
  override cloneNode(subtree?: boolean | undefined): Node;
  override compareDocumentPosition(other: Node): number;
  override contains(other: Node | null): boolean;
  override getRootNode(options?: GetRootNodeOptions | undefined): Node;
  override hasChildNodes(): boolean;
  override insertBefore<T extends Node>(node: T, child: Node | null): T;
  override isDefaultNamespace(namespace: string | null): boolean;
  override isEqualNode(otherNode: Node | null): boolean;
  override isSameNode(otherNode: Node | null): boolean;
  override lookupNamespaceURI(prefix: string | null): string | null;
  override lookupPrefix(namespace: string | null): string | null;
  override normalize(): void;
  override removeChild<T extends Node>(child: T): T;
  override replaceChild<T extends Node>(node: Node, child: T): T;
  readonly override ELEMENT_NODE: 1;
  readonly override ATTRIBUTE_NODE: 2;
  readonly override TEXT_NODE: 3;
  readonly override CDATA_SECTION_NODE: 4;
  readonly override ENTITY_REFERENCE_NODE: 5;
  readonly override ENTITY_NODE: 6;
  readonly override PROCESSING_INSTRUCTION_NODE: 7;
  readonly override COMMENT_NODE: 8;
  readonly override DOCUMENT_NODE: 9;
  readonly override DOCUMENT_TYPE_NODE: 10;
  readonly override DOCUMENT_FRAGMENT_NODE: 11;
  readonly override NOTATION_NODE: 12;
  readonly override DOCUMENT_POSITION_DISCONNECTED: 1;
  readonly override DOCUMENT_POSITION_PRECEDING: 2;
  readonly override DOCUMENT_POSITION_FOLLOWING: 4;
  readonly override DOCUMENT_POSITION_CONTAINS: 8;
  readonly override DOCUMENT_POSITION_CONTAINED_BY: 16;
  readonly override DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: 32;
  override dispatchEvent(event: Event): boolean;
  optional override removeAllListeners(eventName?: string | undefined): void;
  optional override eventListeners(eventName?: string | undefined): EventListenerOrEventListenerObject[];
  override ariaActiveDescendantElement: Element | null;
  override ariaAtomic: string | null;
  override ariaAutoComplete: string | null;
  override ariaBrailleLabel: string | null;
  override ariaBrailleRoleDescription: string | null;
  override ariaBusy: string | null;
  override ariaChecked: string | null;
  override ariaColCount: string | null;
  override ariaColIndex: string | null;
  override ariaColIndexText: string | null;
  override ariaColSpan: string | null;
  override ariaControlsElements: readonly Element[] | null;
  override ariaCurrent: string | null;
  override ariaDescribedByElements: readonly Element[] | null;
  override ariaDescription: string | null;
  override ariaDetailsElements: readonly Element[] | null;
  override ariaDisabled: string | null;
  override ariaErrorMessageElements: readonly Element[] | null;
  override ariaExpanded: string | null;
  override ariaFlowToElements: readonly Element[] | null;
  override ariaHasPopup: string | null;
  override ariaHidden: string | null;
  override ariaInvalid: string | null;
  override ariaKeyShortcuts: string | null;
  override ariaLabel: string | null;
  override ariaLabelledByElements: readonly Element[] | null;
  override ariaLevel: string | null;
  override ariaLive: string | null;
  override ariaModal: string | null;
  override ariaMultiLine: string | null;
  override ariaMultiSelectable: string | null;
  override ariaOrientation: string | null;
  override ariaOwnsElements: readonly Element[] | null;
  override ariaPlaceholder: string | null;
  override ariaPosInSet: string | null;
  override ariaPressed: string | null;
  override ariaReadOnly: string | null;
  override ariaRelevant: string | null;
  override ariaRequired: string | null;
  override ariaRoleDescription: string | null;
  override ariaRowCount: string | null;
  override ariaRowIndex: string | null;
  override ariaRowIndexText: string | null;
  override ariaRowSpan: string | null;
  override ariaSelected: string | null;
  override ariaSetSize: string | null;
  override ariaSort: string | null;
  override ariaValueMax: string | null;
  override ariaValueMin: string | null;
  override ariaValueNow: string | null;
  override ariaValueText: string | null;
  override role: string | null;
  override animate(keyframes: Keyframe[] | PropertyIndexedKeyframes | null, options?: number | KeyframeAnimationOptions | undefined): Animation;
  override getAnimations(options?: GetAnimationsOptions | undefined): Animation[];
  override after(...nodes: (string | Node)[]): void;
  override before(...nodes: (string | Node)[]): void;
  override remove(): void;
  override replaceWith(...nodes: (string | Node)[]): void;
  readonly override nextElementSibling: Element | null;
  readonly override previousElementSibling: Element | null;
  readonly override childElementCount: number;
  readonly override children: HTMLCollection;
  readonly override firstElementChild: Element | null;
  readonly override lastElementChild: Element | null;
  override append(...nodes: (string | Node)[]): void;
  override prepend(...nodes: (string | Node)[]): void;
  override querySelector<K extends keyof HTMLElementTagNameMap>(selectors: K): HTMLElementTagNameMap[K] | null;
  override querySelector<K extends keyof SVGElementTagNameMap>(selectors: K): SVGElementTagNameMap[K] | null;
  override querySelector<K extends keyof MathMLElementTagNameMap>(selectors: K): MathMLElementTagNameMap[K] | null;
  override querySelector<K extends keyof HTMLElementDeprecatedTagNameMap>(selectors: K): HTMLElementDeprecatedTagNameMap[K] | null;
  override querySelector<E extends Element = Element>(selectors: string): E | null;
  override querySelectorAll<K extends keyof HTMLElementTagNameMap>(selectors: K): NodeListOf<HTMLElementTagNameMap[K]>;
  override querySelectorAll<K extends keyof SVGElementTagNameMap>(selectors: K): NodeListOf<SVGElementTagNameMap[K]>;
  override querySelectorAll<K extends keyof MathMLElementTagNameMap>(selectors: K): NodeListOf<MathMLElementTagNameMap[K]>;
  override querySelectorAll<K extends keyof HTMLElementDeprecatedTagNameMap>(selectors: K): NodeListOf<HTMLElementDeprecatedTagNameMap[K]>;
  override querySelectorAll<E extends Element = Element>(selectors: string): NodeListOf<E>;
  override replaceChildren(...nodes: (string | Node)[]): void;
  readonly override assignedSlot: HTMLSlotElement | null;
  readonly override attributeStyleMap: StylePropertyMap;
  override get style(): CSSStyleDeclaration;
  override contentEditable: string;
  override enterKeyHint: string;
  override inputMode: string;
  readonly override isContentEditable: boolean;
  override onabort: ((this: GlobalEventHandlers, ev: UIEvent) => any) | null;
  override onanimationcancel: ((this: GlobalEventHandlers, ev: AnimationEvent) => any) | null;
  override onanimationend: ((this: GlobalEventHandlers, ev: AnimationEvent) => any) | null;
  override onanimationiteration: ((this: GlobalEventHandlers, ev: AnimationEvent) => any) | null;
  override onanimationstart: ((this: GlobalEventHandlers, ev: AnimationEvent) => any) | null;
  override onauxclick: ((this: GlobalEventHandlers, ev: PointerEvent) => any) | null;
  override onbeforeinput: ((this: GlobalEventHandlers, ev: InputEvent) => any) | null;
  override onbeforematch: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onbeforetoggle: ((this: GlobalEventHandlers, ev: ToggleEvent) => any) | null;
  override onblur: ((this: GlobalEventHandlers, ev: FocusEvent) => any) | null;
  override oncancel: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override oncanplay: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override oncanplaythrough: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onchange: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onclick: ((this: GlobalEventHandlers, ev: PointerEvent) => any) | null;
  override onclose: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override oncontextlost: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override oncontextmenu: ((this: GlobalEventHandlers, ev: PointerEvent) => any) | null;
  override oncontextrestored: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override oncopy: ((this: GlobalEventHandlers, ev: ClipboardEvent) => any) | null;
  override oncuechange: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override oncut: ((this: GlobalEventHandlers, ev: ClipboardEvent) => any) | null;
  override ondblclick: ((this: GlobalEventHandlers, ev: MouseEvent) => any) | null;
  override ondrag: ((this: GlobalEventHandlers, ev: DragEvent) => any) | null;
  override ondragend: ((this: GlobalEventHandlers, ev: DragEvent) => any) | null;
  override ondragenter: ((this: GlobalEventHandlers, ev: DragEvent) => any) | null;
  override ondragleave: ((this: GlobalEventHandlers, ev: DragEvent) => any) | null;
  override ondragover: ((this: GlobalEventHandlers, ev: DragEvent) => any) | null;
  override ondragstart: ((this: GlobalEventHandlers, ev: DragEvent) => any) | null;
  override ondrop: ((this: GlobalEventHandlers, ev: DragEvent) => any) | null;
  override ondurationchange: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onemptied: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onended: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onerror: OnErrorEventHandler;
  override onfocus: ((this: GlobalEventHandlers, ev: FocusEvent) => any) | null;
  override onformdata: ((this: GlobalEventHandlers, ev: FormDataEvent) => any) | null;
  override ongotpointercapture: ((this: GlobalEventHandlers, ev: PointerEvent) => any) | null;
  override oninput: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override oninvalid: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onkeydown: ((this: GlobalEventHandlers, ev: KeyboardEvent) => any) | null;
  override onkeypress: ((this: GlobalEventHandlers, ev: KeyboardEvent) => any) | null;
  override onkeyup: ((this: GlobalEventHandlers, ev: KeyboardEvent) => any) | null;
  override onload: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onloadeddata: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onloadedmetadata: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onloadstart: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onlostpointercapture: ((this: GlobalEventHandlers, ev: PointerEvent) => any) | null;
  override onmousedown: ((this: GlobalEventHandlers, ev: MouseEvent) => any) | null;
  override onmouseenter: ((this: GlobalEventHandlers, ev: MouseEvent) => any) | null;
  override onmouseleave: ((this: GlobalEventHandlers, ev: MouseEvent) => any) | null;
  override onmousemove: ((this: GlobalEventHandlers, ev: MouseEvent) => any) | null;
  override onmouseout: ((this: GlobalEventHandlers, ev: MouseEvent) => any) | null;
  override onmouseover: ((this: GlobalEventHandlers, ev: MouseEvent) => any) | null;
  override onmouseup: ((this: GlobalEventHandlers, ev: MouseEvent) => any) | null;
  override onpaste: ((this: GlobalEventHandlers, ev: ClipboardEvent) => any) | null;
  override onpause: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onplay: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onplaying: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onpointercancel: ((this: GlobalEventHandlers, ev: PointerEvent) => any) | null;
  override onpointerdown: ((this: GlobalEventHandlers, ev: PointerEvent) => any) | null;
  override onpointerenter: ((this: GlobalEventHandlers, ev: PointerEvent) => any) | null;
  override onpointerleave: ((this: GlobalEventHandlers, ev: PointerEvent) => any) | null;
  override onpointermove: ((this: GlobalEventHandlers, ev: PointerEvent) => any) | null;
  override onpointerout: ((this: GlobalEventHandlers, ev: PointerEvent) => any) | null;
  override onpointerover: ((this: GlobalEventHandlers, ev: PointerEvent) => any) | null;
  override onpointerrawupdate: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onpointerup: ((this: GlobalEventHandlers, ev: PointerEvent) => any) | null;
  override onprogress: ((this: GlobalEventHandlers, ev: ProgressEvent<EventTarget>) => any) | null;
  override onratechange: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onreset: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onresize: ((this: GlobalEventHandlers, ev: UIEvent) => any) | null;
  override onscroll: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onscrollend: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onsecuritypolicyviolation: ((this: GlobalEventHandlers, ev: SecurityPolicyViolationEvent) => any) | null;
  override onseeked: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onseeking: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onselect: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onselectionchange: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onselectstart: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onslotchange: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onstalled: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onsubmit: ((this: GlobalEventHandlers, ev: SubmitEvent) => any) | null;
  override onsuspend: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override ontimeupdate: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override ontoggle: ((this: GlobalEventHandlers, ev: ToggleEvent) => any) | null;
  override ontouchcancel?: ((this: GlobalEventHandlers, ev: TouchEvent) => any) | null | undefined;
  override ontouchend?: ((this: GlobalEventHandlers, ev: TouchEvent) => any) | null | undefined;
  override ontouchmove?: ((this: GlobalEventHandlers, ev: TouchEvent) => any) | null | undefined;
  override ontouchstart?: ((this: GlobalEventHandlers, ev: TouchEvent) => any) | null | undefined;
  override ontransitioncancel: ((this: GlobalEventHandlers, ev: TransitionEvent) => any) | null;
  override ontransitionend: ((this: GlobalEventHandlers, ev: TransitionEvent) => any) | null;
  override ontransitionrun: ((this: GlobalEventHandlers, ev: TransitionEvent) => any) | null;
  override ontransitionstart: ((this: GlobalEventHandlers, ev: TransitionEvent) => any) | null;
  override onvolumechange: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onwaiting: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onwebkitanimationend: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onwebkitanimationiteration: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onwebkitanimationstart: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onwebkittransitionend: ((this: GlobalEventHandlers, ev: Event) => any) | null;
  override onwheel: ((this: GlobalEventHandlers, ev: WheelEvent) => any) | null;
  override autofocus: boolean;
  readonly override dataset: DOMStringMap;
  override nonce?: string | undefined;
  override tabIndex: number;
  override blur(): void;
  override focus(options?: FocusOptions | undefined): void;
}
```

### ngElementStrategy

`NgElementStrategy`

The strategy that controls how a component is transformed in a custom element.

### ngElementEventsSubscription

`any`

A subscription to change, connect, and disconnect events in the custom element.

### attributeChangedCallback

`void`

Prototype for a handler that responds to a change in an observed attribute.

@paramattrName`string`

The name of the attribute that has changed.

@paramoldValue`string | null`

The previous value of the attribute.

@paramnewValue`string`

The new value of the attribute.

@paramnamespace`string | undefined`

The namespace in which the attribute is defined.

@returns`void`

### connectedCallback

`void`

Prototype for a handler that responds to the insertion of the custom element in the DOM.

@returns`void`

### disconnectedCallback

`void`

Prototype for a handler that responds to the deletion of the custom element from the DOM.

@returns`void`

### accessKey

`string`

The **`HTMLElement.accessKey`** property sets the keystroke which a user can press to jump to a given element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/accessKey)

### accessKeyLabel

`string`

The **`HTMLElement.accessKeyLabel`** read-only property returns a string containing the element's browser-assigned access key (if any); otherwise it returns an empty string.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/accessKeyLabel)

### autocapitalize

`string`

The **`autocapitalize`** property of the HTMLElement interface represents the element's capitalization behavior for user input.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/autocapitalize)

### autocorrect

`boolean`

The **`autocorrect`** property of the HTMLElement interface controls whether or not autocorrection of editable text is enabled for spelling and/or punctuation errors.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/autocorrect)

### dir

`string`

The **`HTMLElement.dir`** property indicates the text writing directionality of the content of the current element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/dir)

### draggable

`boolean`

The **`draggable`** property of the HTMLElement interface gets and sets a Boolean primitive indicating if the element is draggable.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/draggable)

### hidden

`boolean`

The HTMLElement property **`hidden`** reflects the value of the element's `hidden` attribute.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/hidden)

### inert

`boolean`

The HTMLElement property **`inert`** reflects the value of the element's `inert` attribute.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/inert)

### innerText

`string`

The **`innerText`** property of the HTMLElement interface represents the rendered text content of a node and its descendants.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/innerText)

### lang

`string`

The **`lang`** property of the HTMLElement interface indicates the base language of an element's attribute values and text content, in the form of a MISSING: RFC(5646, 'BCP 47 language identifier tag')].

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/lang)

### offsetHeight

`number`

The **`offsetHeight`** read-only property of the HTMLElement interface returns the height of an element, including vertical padding and borders, as an integer.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/offsetHeight)

### offsetLeft

`number`

The **`offsetLeft`** read-only property of the HTMLElement interface returns the number of pixels that the *upper left corner* of the current element is offset to the left within the HTMLElement.offsetParent node.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/offsetLeft)

### offsetParent

`Element | null`

The **`HTMLElement.offsetParent`** read-only property returns a reference to the element which is the closest (nearest in the containment hierarchy) positioned ancestor element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/offsetParent)

### offsetTop

`number`

The **`offsetTop`** read-only property of the HTMLElement interface returns the distance from the outer border of the current element (including its margin) to the top padding edge of the HTMLelement.offsetParent, the *closest positioned* ancestor element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/offsetTop)

### offsetWidth

`number`

The **`offsetWidth`** read-only property of the HTMLElement interface returns the layout width of an element as an integer.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/offsetWidth)

### outerText

`string`

The **`outerText`** property of the HTMLElement interface returns the same value as HTMLElement.innerText.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/outerText)

### popover

`string | null`

The **`popover`** property of the HTMLElement interface gets and sets an element's popover state via JavaScript (`'auto'`, `'hint'`, or `'manual'`), and can be used for feature detection.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/popover)

### spellcheck

`boolean`

The **`spellcheck`** property of the HTMLElement interface represents a boolean value that controls the spell-checking hint.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/spellcheck)

### title

`string`

The **`HTMLElement.title`** property represents the title of the element: the text usually displayed in a 'tooltip' popup when the mouse is over the node.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/title)

### translate

`boolean`

The **`translate`** property of the HTMLElement interface indicates whether an element's attribute values and the values of its Text node children are to be translated when the page is localized, or whether to leave them unchanged.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/translate)

### writingSuggestions

`string`

The **`writingSuggestions`** property of the HTMLElement interface is a string indicating if browser-provided writing suggestions should be enabled under the scope of the element or not.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/writingSuggestions)

### attachInternals

`ElementInternals`

The **`HTMLElement.attachInternals()`** method returns an ElementInternals object.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/attachInternals)

@returns`ElementInternals`

### click

`void`

The **`HTMLElement.click()`** method simulates a mouse click on an element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/click)

@returns`void`

### hidePopover

`void`

The **`hidePopover()`** method of the HTMLElement interface hides a popover element (i.e., one that has a valid `popover` attribute) by removing it from the top layer and styling it with `display: none`.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/hidePopover)

@returns`void`

### showPopover

`void`

The **`showPopover()`** method of the HTMLElement interface shows a Popover\_API element (i.e., one that has a valid `popover` attribute) by adding it to the top layer.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/showPopover)

@returns`void`

### togglePopover

`boolean`

The **`togglePopover()`** method of the HTMLElement interface toggles a Popover\_API element (i.e., one that has a valid `popover` attribute) between the hidden and showing states.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/togglePopover)

@paramoptions`boolean | undefined`

@returns`boolean`

### addEventListener

`void`

@paramtype`K`

@paramlistener`(this: HTMLElement, ev: HTMLElementEventMap[K]) => any`

@paramoptions`boolean | AddEventListenerOptions | undefined`

@returns`void`

### addEventListener

`void`

@paramtype`string`

@paramlistener`EventListenerOrEventListenerObject`

@paramoptions`boolean | AddEventListenerOptions | undefined`

@returns`void`

### removeEventListener

`void`

@paramtype`K`

@paramlistener`(this: HTMLElement, ev: HTMLElementEventMap[K]) => any`

@paramoptions`boolean | EventListenerOptions | undefined`

@returns`void`

### removeEventListener

`void`

@paramtype`string`

@paramlistener`EventListenerOrEventListenerObject`

@paramoptions`boolean | EventListenerOptions | undefined`

@returns`void`

### attributes

`NamedNodeMap`

The **`Element.attributes`** property returns a live collection of all attribute nodes registered to the specified node.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/attributes)

### classList

`DOMTokenList`

The **`Element.classList`** is a read-only property that returns a live DOMTokenList collection of the `class` attributes of the element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/classList)

### classList

`DOMTokenList`

### className

`string`

The **`className`** property of the of the specified element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/className)

### clientHeight

`number`

The **`clientHeight`** read-only property of the Element interface is zero for elements with no CSS or inline layout boxes; otherwise, it's the inner height of an element in pixels.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/clientHeight)

### clientLeft

`number`

The **`clientLeft`** read-only property of the Element interface returns the width of the left border of an element in pixels.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/clientLeft)

### clientTop

`number`

The **`clientTop`** read-only property of the Element interface returns the width of the top border of an element in pixels.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/clientTop)

### clientWidth

`number`

The **`clientWidth`** read-only property of the Element interface is zero for inline elements and elements with no CSS; otherwise, it's the inner width of an element in pixels.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/clientWidth)

### currentCSSZoom

`number`

The **`currentCSSZoom`** read-only property of the Element interface provides the 'effective' CSS `zoom` of an element, taking into account the zoom applied to the element and all its parent elements.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/currentCSSZoom)

### id

`string`

The **`id`** property of the Element interface represents the element's identifier, reflecting the **`id`** global attribute.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/id)

### innerHTML

`string`

The **`innerHTML`** property of the Element interface gets or sets the HTML or XML markup contained within the element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/innerHTML)

### localName

`string`

The **`Element.localName`** read-only property returns the local part of the qualified name of an element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/localName)

### namespaceURI

`string | null`

The **`Element.namespaceURI`** read-only property returns the namespace URI of the element, or `null` if the element is not in a namespace.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/namespaceURI)

### onfullscreenchange

`((this: Element, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/fullscreenchange_event)

### onfullscreenerror

`((this: Element, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/fullscreenerror_event)

### outerHTML

`string`

The **`outerHTML`** attribute of the Element DOM interface gets the serialized HTML fragment describing the element including its descendants.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/outerHTML)

### ownerDocument

`Document`

### part

`DOMTokenList`

The **`part`** property of the Element interface represents the part identifier(s) of the element (i.e., set using the `part` attribute), returned as a DOMTokenList.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/part)

### part

`DOMTokenList`

### prefix

`string | null`

The **`Element.prefix`** read-only property returns the namespace prefix of the specified element, or `null` if no prefix is specified.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/prefix)

### scrollHeight

`number`

The **`scrollHeight`** read-only property of the Element interface is a measurement of the height of an element's content, including content not visible on the screen due to overflow.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollHeight)

### scrollLeft

`number`

The **`scrollLeft`** property of the Element interface gets or sets the number of pixels by which an element's content is scrolled from its left edge.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollLeft)

### scrollTop

`number`

The **`scrollTop`** property of the Element interface gets or sets the number of pixels by which an element's content is scrolled from its top edge.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollTop)

### scrollWidth

`number`

The **`scrollWidth`** read-only property of the Element interface is a measurement of the width of an element's content, including content not visible on the screen due to overflow.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollWidth)

### shadowRoot

`ShadowRoot | null`

The `Element.shadowRoot` read-only property represents the shadow root hosted by the element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/shadowRoot)

### slot

`string`

The **`slot`** property of the Element interface returns the name of the shadow DOM slot the element is inserted in.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/slot)

### tagName

`string`

The **`tagName`** read-only property of the Element interface returns the tag name of the element on which it's called.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/tagName)

### attachShadow

`ShadowRoot`

The **`Element.attachShadow()`** method attaches a shadow DOM tree to the specified element and returns a reference to its ShadowRoot.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/attachShadow)

@paraminit`ShadowRootInit`

@returns`ShadowRoot`

### checkVisibility

`boolean`

The **`checkVisibility()`** method of the Element interface checks whether the element is visible.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/checkVisibility)

@paramoptions`CheckVisibilityOptions | undefined`

@returns`boolean`

### closest

`HTMLElementTagNameMap[K] | null`

The **`closest()`** method of the Element interface traverses the element and its parents (heading toward the document root) until it finds a node that matches the specified CSS selector.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/closest)

@paramselector`K`

@returns`HTMLElementTagNameMap[K] | null`

### closest

`SVGElementTagNameMap[K] | null`

@paramselector`K`

@returns`SVGElementTagNameMap[K] | null`

### closest

`MathMLElementTagNameMap[K] | null`

@paramselector`K`

@returns`MathMLElementTagNameMap[K] | null`

### closest

`E | null`

@paramselectors`string`

@returns`E | null`

### computedStyleMap

`StylePropertyMapReadOnly`

The **`computedStyleMap()`** method of the Element interface returns a StylePropertyMapReadOnly interface which provides a read-only representation of a CSS declaration block that is an alternative to CSSStyleDeclaration.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/computedStyleMap)

@returns`StylePropertyMapReadOnly`

### getAttribute

`string | null`

The **`getAttribute()`** method of the element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getAttribute)

@paramqualifiedName`string`

@returns`string | null`

### getAttributeNS

`string | null`

The **`getAttributeNS()`** method of the Element interface returns the string value of the attribute with the specified namespace and name.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getAttributeNS)

@paramnamespace`string | null`

@paramlocalName`string`

@returns`string | null`

### getAttributeNames

`string[]`

The **`getAttributeNames()`** method of the array.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getAttributeNames)

@returns`string[]`

### getAttributeNode

`Attr | null`

Returns the specified attribute of the specified element, as an Attr node.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getAttributeNode)

@paramqualifiedName`string`

@returns`Attr | null`

### getAttributeNodeNS

`Attr | null`

The **`getAttributeNodeNS()`** method of the Element interface returns the namespaced Attr node of an element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getAttributeNodeNS)

@paramnamespace`string | null`

@paramlocalName`string`

@returns`Attr | null`

### getBoundingClientRect

`DOMRect`

The **`Element.getBoundingClientRect()`** method returns a position relative to the viewport.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getBoundingClientRect)

@returns`DOMRect`

### getClientRects

`DOMRectList`

The **`getClientRects()`** method of the Element interface returns a collection of DOMRect objects that indicate the bounding rectangles for each CSS border box in a client.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getClientRects)

@returns`DOMRectList`

### getElementsByClassName

`HTMLCollectionOf<Element>`

The Element method **`getElementsByClassName()`** returns a live specified class name or names.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getElementsByClassName)

@paramclassNames`string`

@returns`HTMLCollectionOf<Element>`

### getElementsByTagName

`HTMLCollectionOf<HTMLElementTagNameMap[K]>`

The **`Element.getElementsByTagName()`** method returns a live All descendants of the specified element are searched, but not the element itself.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getElementsByTagName)

@paramqualifiedName`K`

@returns`HTMLCollectionOf<HTMLElementTagNameMap[K]>`

### getElementsByTagName

`HTMLCollectionOf<SVGElementTagNameMap[K]>`

@paramqualifiedName`K`

@returns`HTMLCollectionOf<SVGElementTagNameMap[K]>`

### getElementsByTagName

`HTMLCollectionOf<MathMLElementTagNameMap[K]>`

@paramqualifiedName`K`

@returns`HTMLCollectionOf<MathMLElementTagNameMap[K]>`

### getElementsByTagName

`HTMLCollectionOf<HTMLElementDeprecatedTagNameMap[K]>`

@deprecated

@paramqualifiedName`K`

@returns`HTMLCollectionOf<HTMLElementDeprecatedTagNameMap[K]>`

### getElementsByTagName

`HTMLCollectionOf<Element>`

@paramqualifiedName`string`

@returns`HTMLCollectionOf<Element>`

### getElementsByTagNameNS

`HTMLCollectionOf<HTMLElement>`

The **`Element.getElementsByTagNameNS()`** method returns a live HTMLCollection of elements with the given tag name belonging to the given namespace.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getElementsByTagNameNS)

@paramnamespaceURI`"http://www.w3.org/1999/xhtml"`

@paramlocalName`string`

@returns`HTMLCollectionOf<HTMLElement>`

### getElementsByTagNameNS

`HTMLCollectionOf<SVGElement>`

@paramnamespaceURI`"http://www.w3.org/2000/svg"`

@paramlocalName`string`

@returns`HTMLCollectionOf<SVGElement>`

### getElementsByTagNameNS

`HTMLCollectionOf<MathMLElement>`

@paramnamespaceURI`"http://www.w3.org/1998/Math/MathML"`

@paramlocalName`string`

@returns`HTMLCollectionOf<MathMLElement>`

### getElementsByTagNameNS

`HTMLCollectionOf<Element>`

@paramnamespace`string | null`

@paramlocalName`string`

@returns`HTMLCollectionOf<Element>`

### getHTML

`string`

The **`getHTML()`** method of the Element interface is used to serialize an element's DOM to an HTML string.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getHTML)

@paramoptions`GetHTMLOptions | undefined`

@returns`string`

### hasAttribute

`boolean`

The **`Element.hasAttribute()`** method returns a **Boolean** value indicating whether the specified element has the specified attribute or not.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/hasAttribute)

@paramqualifiedName`string`

@returns`boolean`

### hasAttributeNS

`boolean`

The **`hasAttributeNS()`** method of the Element interface returns a boolean value indicating whether the current element has the specified attribute with the specified namespace.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/hasAttributeNS)

@paramnamespace`string | null`

@paramlocalName`string`

@returns`boolean`

### hasAttributes

`boolean`

The **`hasAttributes()`** method of the Element interface returns a boolean value indicating whether the current element has any attributes or not.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/hasAttributes)

@returns`boolean`

### hasPointerCapture

`boolean`

The **`hasPointerCapture()`** method of the pointer capture for the pointer identified by the given pointer ID.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/hasPointerCapture)

@parampointerId`number`

@returns`boolean`

### insertAdjacentElement

`Element | null`

The **`insertAdjacentElement()`** method of the relative to the element it is invoked upon.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/insertAdjacentElement)

@paramwhere`InsertPosition`

@paramelement`Element`

@returns`Element | null`

### insertAdjacentHTML

`void`

The **`insertAdjacentHTML()`** method of the the resulting nodes into the DOM tree at a specified position.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/insertAdjacentHTML)

@paramposition`InsertPosition`

@paramstring`string`

@returns`void`

### insertAdjacentText

`void`

The **`insertAdjacentText()`** method of the Element interface, given a relative position and a string, inserts a new text node at the given position relative to the element it is called from.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/insertAdjacentText)

@paramwhere`InsertPosition`

@paramdata`string`

@returns`void`

### matches

`boolean`

The **`matches()`** method of the Element interface tests whether the element would be selected by the specified CSS selector.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/matches)

@paramselectors`string`

@returns`boolean`

### releasePointerCapture

`void`

The **`releasePointerCapture()`** method of the previously set for a specific (PointerEvent) *pointer*.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/releasePointerCapture)

@parampointerId`number`

@returns`void`

### removeAttribute

`void`

The Element method **`removeAttribute()`** removes the attribute with the specified name from the element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/removeAttribute)

@paramqualifiedName`string`

@returns`void`

### removeAttributeNS

`void`

The **`removeAttributeNS()`** method of the If you are working with HTML and you don't need to specify the requested attribute as being part of a specific namespace, use the Element.removeAttribute() method instead.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/removeAttributeNS)

@paramnamespace`string | null`

@paramlocalName`string`

@returns`void`

### removeAttributeNode

`Attr`

The **`removeAttributeNode()`** method of the Element interface removes the specified Attr node from the element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/removeAttributeNode)

@paramattr`Attr`

@returns`Attr`

### requestFullscreen

`Promise<void>`

The **`Element.requestFullscreen()`** method issues an asynchronous request to make the element be displayed in fullscreen mode.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/requestFullscreen)

@paramoptions`FullscreenOptions | undefined`

@returns`Promise<void>`

### requestPointerLock

`Promise<void>`

The **`requestPointerLock()`** method of the Element interface lets you asynchronously ask for the pointer to be locked on the given element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/requestPointerLock)

@paramoptions`PointerLockOptions | undefined`

@returns`Promise<void>`

### scroll

`void`

The **`scroll()`** method of the Element interface scrolls the element to a particular set of coordinates inside a given element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scroll)

@paramoptions`ScrollToOptions | undefined`

@returns`void`

### scroll

`void`

@paramx`number`

@paramy`number`

@returns`void`

### scrollBy

`void`

The **`scrollBy()`** method of the Element interface scrolls an element by the given amount.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollBy)

@paramoptions`ScrollToOptions | undefined`

@returns`void`

### scrollBy

`void`

@paramx`number`

@paramy`number`

@returns`void`

### scrollIntoView

`void`

The Element interface's **`scrollIntoView()`** method scrolls the element's ancestor containers such that the element on which `scrollIntoView()` is called is visible to the user.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollIntoView)

@paramarg`boolean | ScrollIntoViewOptions | undefined`

@returns`void`

### scrollTo

`void`

The **`scrollTo()`** method of the Element interface scrolls to a particular set of coordinates inside a given element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/scrollTo)

@paramoptions`ScrollToOptions | undefined`

@returns`void`

### scrollTo

`void`

@paramx`number`

@paramy`number`

@returns`void`

### setAttribute

`void`

The **`setAttribute()`** method of the Element interface sets the value of an attribute on the specified element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/setAttribute)

@paramqualifiedName`string`

@paramvalue`string`

@returns`void`

### setAttributeNS

`void`

`setAttributeNS` adds a new attribute or changes the value of an attribute with the given namespace and name.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/setAttributeNS)

@paramnamespace`string | null`

@paramqualifiedName`string`

@paramvalue`string`

@returns`void`

### setAttributeNode

`Attr | null`

The **`setAttributeNode()`** method of the Element interface adds a new Attr node to the specified element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/setAttributeNode)

@paramattr`Attr`

@returns`Attr | null`

### setAttributeNodeNS

`Attr | null`

The **`setAttributeNodeNS()`** method of the Element interface adds a new namespaced Attr node to an element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/setAttributeNodeNS)

@paramattr`Attr`

@returns`Attr | null`

### setHTMLUnsafe

`void`

The **`setHTMLUnsafe()`** method of the Element interface is used to parse a string of HTML into a DocumentFragment, optionally filtering out unwanted elements and attributes, and those that don't belong in the context, and then using it to replace the element's subtree in the DOM.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/setHTMLUnsafe)

@paramhtml`string`

@returns`void`

### setPointerCapture

`void`

The **`setPointerCapture()`** method of the *capture target* of future pointer events.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/setPointerCapture)

@parampointerId`number`

@returns`void`

### toggleAttribute

`boolean`

The **`toggleAttribute()`** method of the present and adding it if it is not present) on the given element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/toggleAttribute)

@paramqualifiedName`string`

@paramforce`boolean | undefined`

@returns`boolean`

### webkitMatchesSelector

`boolean`

@deprecated

This is a legacy alias of `matches`.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/matches)

@paramselectors`string`

@returns`boolean`

### textContent

`string`

[MDN Reference](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent)

### textContent

`string`

### baseURI

`string`

The read-only **`baseURI`** property of the Node interface returns the absolute base URL of the document containing the node.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/baseURI)

### childNodes

`NodeListOf<ChildNode>`

The read-only **`childNodes`** property of the Node interface returns a live the first child node is assigned index `0`.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/childNodes)

### firstChild

`ChildNode | null`

The read-only **`firstChild`** property of the Node interface returns the node's first child in the tree, or `null` if the node has no children.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/firstChild)

### isConnected

`boolean`

The read-only **`isConnected`** property of the Node interface returns a boolean indicating whether the node is connected (directly or indirectly) to a Document object.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/isConnected)

### lastChild

`ChildNode | null`

The read-only **`lastChild`** property of the Node interface returns the last child of the node, or `null` if there are no child nodes.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/lastChild)

### nextSibling

`ChildNode | null`

The read-only **`nextSibling`** property of the Node interface returns the node immediately following the specified one in their parent's Node.childNodes, or returns `null` if the specified node is the last child in the parent element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/nextSibling)

### nodeName

`string`

The read-only **`nodeName`** property of Node returns the name of the current node as a string.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/nodeName)

### nodeType

`number`

The read-only **`nodeType`** property of a Node interface is an integer that identifies what the node is.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/nodeType)

### nodeValue

`string | null`

The **`nodeValue`** property of the Node interface returns or sets the value of the current node.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/nodeValue)

### parentElement

`HTMLElement | null`

The read-only **`parentElement`** property of Node interface returns the DOM node's parent Element, or `null` if the node either has no parent, or its parent isn't a DOM Element.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/parentElement)

### parentNode

`ParentNode | null`

The read-only **`parentNode`** property of the Node interface returns the parent of the specified node in the DOM tree.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/parentNode)

### previousSibling

`ChildNode | null`

The read-only **`previousSibling`** property of the Node interface returns the node immediately preceding the specified one in its parent's or `null` if the specified node is the first in that list.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/previousSibling)

### appendChild

`T`

The **`appendChild()`** method of the Node interface adds a node to the end of the list of children of a specified parent node.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/appendChild)

@paramnode`T`

@returns`T`

### cloneNode

`Node`

The **`cloneNode()`** method of the Node interface returns a duplicate of the node on which this method was called.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/cloneNode)

@paramsubtree`boolean | undefined`

@returns`Node`

### compareDocumentPosition

`number`

The **`compareDocumentPosition()`** method of the Node interface reports the position of its argument node relative to the node on which it is called.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/compareDocumentPosition)

@paramother`Node`

@returns`number`

### contains

`boolean`

The **`contains()`** method of the Node interface returns a boolean value indicating whether a node is a descendant of a given node, that is the node itself, one of its direct children (Node.childNodes), one of the children's direct children, and so on.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/contains)

@paramother`Node | null`

@returns`boolean`

### getRootNode

`Node`

The **`getRootNode()`** method of the Node interface returns the context object's root, which optionally includes the shadow root if it is available.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/getRootNode)

@paramoptions`GetRootNodeOptions | undefined`

@returns`Node`

### hasChildNodes

`boolean`

The **`hasChildNodes()`** method of the Node interface returns a boolean value indicating whether the given Node has child nodes or not.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/hasChildNodes)

@returns`boolean`

### insertBefore

`T`

The **`insertBefore()`** method of the Node interface inserts a node before a *reference node* as a child of a specified *parent node*.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/insertBefore)

@paramnode`T`

@paramchild`Node | null`

@returns`T`

### isDefaultNamespace

`boolean`

The **`isDefaultNamespace()`** method of the Node interface accepts a namespace URI as an argument.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/isDefaultNamespace)

@paramnamespace`string | null`

@returns`boolean`

### isEqualNode

`boolean`

The **`isEqualNode()`** method of the Node interface tests whether two nodes are equal.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/isEqualNode)

@paramotherNode`Node | null`

@returns`boolean`

### isSameNode

`boolean`

The **`isSameNode()`** method of the Node interface is a legacy alias the for the `===` strict equality operator.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/isSameNode)

@paramotherNode`Node | null`

@returns`boolean`

### lookupNamespaceURI

`string | null`

The **`lookupNamespaceURI()`** method of the Node interface takes a prefix as parameter and returns the namespace URI associated with it on the given node if found (and `null` if not).

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/lookupNamespaceURI)

@paramprefix`string | null`

@returns`string | null`

### lookupPrefix

`string | null`

The **`lookupPrefix()`** method of the Node interface returns a string containing the prefix for a given namespace URI, if present, and `null` if not.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/lookupPrefix)

@paramnamespace`string | null`

@returns`string | null`

### normalize

`void`

The **`normalize()`** method of the Node interface puts the specified node and all of its sub-tree into a *normalized* form.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/normalize)

@returns`void`

### removeChild

`T`

The **`removeChild()`** method of the Node interface removes a child node from the DOM and returns the removed node.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/removeChild)

@paramchild`T`

@returns`T`

### replaceChild

`T`

The **`replaceChild()`** method of the Node interface replaces a child node within the given (parent) node.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/replaceChild)

@paramnode`Node`

@paramchild`T`

@returns`T`

### ELEMENT\_NODE

`1`

node is an element.

### ATTRIBUTE\_NODE

`2`

### TEXT\_NODE

`3`

node is a Text node.

### CDATA\_SECTION\_NODE

`4`

node is a CDATASection node.

### ENTITY\_REFERENCE\_NODE

`5`

### ENTITY\_NODE

`6`

### PROCESSING\_INSTRUCTION\_NODE

`7`

node is a ProcessingInstruction node.

### COMMENT\_NODE

`8`

node is a Comment node.

### DOCUMENT\_NODE

`9`

node is a document.

### DOCUMENT\_TYPE\_NODE

`10`

node is a doctype.

### DOCUMENT\_FRAGMENT\_NODE

`11`

node is a DocumentFragment node.

### NOTATION\_NODE

`12`

### DOCUMENT\_POSITION\_DISCONNECTED

`1`

Set when node and other are not in the same tree.

### DOCUMENT\_POSITION\_PRECEDING

`2`

Set when other is preceding node.

### DOCUMENT\_POSITION\_FOLLOWING

`4`

Set when other is following node.

### DOCUMENT\_POSITION\_CONTAINS

`8`

Set when other is an ancestor of node.

### DOCUMENT\_POSITION\_CONTAINED\_BY

`16`

Set when other is a descendant of node.

### DOCUMENT\_POSITION\_IMPLEMENTATION\_SPECIFIC

`32`

### dispatchEvent

`boolean`

The **`dispatchEvent()`** method of the EventTarget sends an Event to the object, (synchronously) invoking the affected event listeners in the appropriate order.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/EventTarget/dispatchEvent)

@paramevent`Event`

@returns`boolean`

### removeAllListeners

`void`

Remove all event listeners by name for this event target.

This method is optional because it may not be available if you use `noop zone` when bootstrapping Angular application or disable the `EventTarget` monkey patch by `zone.js`.

If the `eventName` is provided, will remove event listeners of that name. If the `eventName` is not provided, will remove all event listeners associated with `EventTarget`.

@parameventName`string | undefined`

the name of the event, such as `click`. This parameter is optional.

@returns`void`

### eventListeners

`EventListenerOrEventListenerObject[]`

Retrieve all event listeners by name.

This method is optional because it may not be available if you use `noop zone` when bootstrapping Angular application or disable the `EventTarget` monkey patch by `zone.js`.

If the `eventName` is provided, will return an array of event handlers or event listener objects of the given event. If the `eventName` is not provided, will return all listeners.

@parameventName`string | undefined`

the name of the event, such as click. This parameter is optional.

@returns`EventListenerOrEventListenerObject[]`

### ariaActiveDescendantElement

`Element | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaActiveDescendantElement)

### ariaAtomic

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaAtomic)

### ariaAutoComplete

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaAutoComplete)

### ariaBrailleLabel

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaBrailleLabel)

### ariaBrailleRoleDescription

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaBrailleRoleDescription)

### ariaBusy

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaBusy)

### ariaChecked

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaChecked)

### ariaColCount

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaColCount)

### ariaColIndex

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaColIndex)

### ariaColIndexText

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaColIndexText)

### ariaColSpan

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaColSpan)

### ariaControlsElements

`readonly Element[] | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaControlsElements)

### ariaCurrent

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaCurrent)

### ariaDescribedByElements

`readonly Element[] | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaDescribedByElements)

### ariaDescription

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaDescription)

### ariaDetailsElements

`readonly Element[] | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaDetailsElements)

### ariaDisabled

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaDisabled)

### ariaErrorMessageElements

`readonly Element[] | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaErrorMessageElements)

### ariaExpanded

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaExpanded)

### ariaFlowToElements

`readonly Element[] | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaFlowToElements)

### ariaHasPopup

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaHasPopup)

### ariaHidden

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaHidden)

### ariaInvalid

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaInvalid)

### ariaKeyShortcuts

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaKeyShortcuts)

### ariaLabel

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaLabel)

### ariaLabelledByElements

`readonly Element[] | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaLabelledByElements)

### ariaLevel

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaLevel)

### ariaLive

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaLive)

### ariaModal

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaModal)

### ariaMultiLine

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaMultiLine)

### ariaMultiSelectable

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaMultiSelectable)

### ariaOrientation

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaOrientation)

### ariaOwnsElements

`readonly Element[] | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaOwnsElements)

### ariaPlaceholder

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaPlaceholder)

### ariaPosInSet

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaPosInSet)

### ariaPressed

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaPressed)

### ariaReadOnly

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaReadOnly)

### ariaRelevant

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaRelevant)

### ariaRequired

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaRequired)

### ariaRoleDescription

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaRoleDescription)

### ariaRowCount

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaRowCount)

### ariaRowIndex

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaRowIndex)

### ariaRowIndexText

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaRowIndexText)

### ariaRowSpan

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaRowSpan)

### ariaSelected

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaSelected)

### ariaSetSize

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaSetSize)

### ariaSort

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaSort)

### ariaValueMax

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaValueMax)

### ariaValueMin

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaValueMin)

### ariaValueNow

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaValueNow)

### ariaValueText

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/ariaValueText)

### role

`string | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/role)

### animate

`Animation`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animate)

@paramkeyframes`Keyframe[] | PropertyIndexedKeyframes | null`

@paramoptions`number | KeyframeAnimationOptions | undefined`

@returns`Animation`

### getAnimations

`Animation[]`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/getAnimations)

@paramoptions`GetAnimationsOptions | undefined`

@returns`Animation[]`

### after

`void`

Inserts nodes just after node, while replacing strings in nodes with equivalent Text nodes.

Throws a "HierarchyRequestError" DOMException if the constraints of the node tree are violated.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/CharacterData/after)

@paramnodes`(string | Node)[]`

@returns`void`

### before

`void`

Inserts nodes just before node, while replacing strings in nodes with equivalent Text nodes.

Throws a "HierarchyRequestError" DOMException if the constraints of the node tree are violated.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/CharacterData/before)

@paramnodes`(string | Node)[]`

@returns`void`

### remove

`void`

Removes node.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/CharacterData/remove)

@returns`void`

### replaceWith

`void`

Replaces node with nodes, while replacing strings in nodes with equivalent Text nodes.

Throws a "HierarchyRequestError" DOMException if the constraints of the node tree are violated.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/CharacterData/replaceWith)

@paramnodes`(string | Node)[]`

@returns`void`

### nextElementSibling

`Element | null`

Returns the first following sibling that is an element, and null otherwise.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/CharacterData/nextElementSibling)

### previousElementSibling

`Element | null`

Returns the first preceding sibling that is an element, and null otherwise.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/CharacterData/previousElementSibling)

### childElementCount

`number`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/childElementCount)

### children

`HTMLCollection`

Returns the child elements.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/children)

### firstElementChild

`Element | null`

Returns the first child that is an element, and null otherwise.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/firstElementChild)

### lastElementChild

`Element | null`

Returns the last child that is an element, and null otherwise.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/lastElementChild)

### append

`void`

Inserts nodes after the last child of node, while replacing strings in nodes with equivalent Text nodes.

Throws a "HierarchyRequestError" DOMException if the constraints of the node tree are violated.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/append)

@paramnodes`(string | Node)[]`

@returns`void`

### prepend

`void`

Inserts nodes before the first child of node, while replacing strings in nodes with equivalent Text nodes.

Throws a "HierarchyRequestError" DOMException if the constraints of the node tree are violated.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/prepend)

@paramnodes`(string | Node)[]`

@returns`void`

### querySelector

`HTMLElementTagNameMap[K] | null`

Returns the first element that is a descendant of node that matches selectors.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/querySelector)

@paramselectors`K`

@returns`HTMLElementTagNameMap[K] | null`

### querySelector

`SVGElementTagNameMap[K] | null`

@paramselectors`K`

@returns`SVGElementTagNameMap[K] | null`

### querySelector

`MathMLElementTagNameMap[K] | null`

@paramselectors`K`

@returns`MathMLElementTagNameMap[K] | null`

### querySelector

`HTMLElementDeprecatedTagNameMap[K] | null`

@deprecated

@paramselectors`K`

@returns`HTMLElementDeprecatedTagNameMap[K] | null`

### querySelector

`E | null`

@paramselectors`string`

@returns`E | null`

### querySelectorAll

`NodeListOf<HTMLElementTagNameMap[K]>`

Returns all element descendants of node that match selectors.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/querySelectorAll)

@paramselectors`K`

@returns`NodeListOf<HTMLElementTagNameMap[K]>`

### querySelectorAll

`NodeListOf<SVGElementTagNameMap[K]>`

@paramselectors`K`

@returns`NodeListOf<SVGElementTagNameMap[K]>`

### querySelectorAll

`NodeListOf<MathMLElementTagNameMap[K]>`

@paramselectors`K`

@returns`NodeListOf<MathMLElementTagNameMap[K]>`

### querySelectorAll

`NodeListOf<HTMLElementDeprecatedTagNameMap[K]>`

@deprecated

@paramselectors`K`

@returns`NodeListOf<HTMLElementDeprecatedTagNameMap[K]>`

### querySelectorAll

`NodeListOf<E>`

@paramselectors`string`

@returns`NodeListOf<E>`

### replaceChildren

`void`

Replace all children of node with nodes, while replacing strings in nodes with equivalent Text nodes.

Throws a "HierarchyRequestError" DOMException if the constraints of the node tree are violated.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/replaceChildren)

@paramnodes`(string | Node)[]`

@returns`void`

### assignedSlot

`HTMLSlotElement | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/assignedSlot)

### attributeStyleMap

`StylePropertyMap`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/attributeStyleMap)

### style

`CSSStyleDeclaration`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/style)

### style

`CSSStyleDeclaration`

### contentEditable

`string`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/contentEditable)

### enterKeyHint

`string`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/enterKeyHint)

### inputMode

`string`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/inputMode)

### isContentEditable

`boolean`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/isContentEditable)

### onabort

`((this: GlobalEventHandlers, ev: UIEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/abort_event)

### onanimationcancel

`((this: GlobalEventHandlers, ev: AnimationEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationcancel_event)

### onanimationend

`((this: GlobalEventHandlers, ev: AnimationEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationend_event)

### onanimationiteration

`((this: GlobalEventHandlers, ev: AnimationEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationiteration_event)

### onanimationstart

`((this: GlobalEventHandlers, ev: AnimationEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationstart_event)

### onauxclick

`((this: GlobalEventHandlers, ev: PointerEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/auxclick_event)

### onbeforeinput

`((this: GlobalEventHandlers, ev: InputEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/beforeinput_event)

### onbeforematch

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/beforematch_event)

### onbeforetoggle

`((this: GlobalEventHandlers, ev: ToggleEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/beforetoggle_event)

### onblur

`((this: GlobalEventHandlers, ev: FocusEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/blur_event)

### oncancel

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLDialogElement/cancel_event)

### oncanplay

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/canplay_event)

### oncanplaythrough

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/canplaythrough_event)

### onchange

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/change_event)

### onclick

`((this: GlobalEventHandlers, ev: PointerEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/click_event)

### onclose

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLDialogElement/close_event)

### oncontextlost

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLCanvasElement/contextlost_event)

### oncontextmenu

`((this: GlobalEventHandlers, ev: PointerEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/contextmenu_event)

### oncontextrestored

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLCanvasElement/contextrestored_event)

### oncopy

`((this: GlobalEventHandlers, ev: ClipboardEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/copy_event)

### oncuechange

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLTrackElement/cuechange_event)

### oncut

`((this: GlobalEventHandlers, ev: ClipboardEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/cut_event)

### ondblclick

`((this: GlobalEventHandlers, ev: MouseEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/dblclick_event)

### ondrag

`((this: GlobalEventHandlers, ev: DragEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/drag_event)

### ondragend

`((this: GlobalEventHandlers, ev: DragEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/dragend_event)

### ondragenter

`((this: GlobalEventHandlers, ev: DragEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/dragenter_event)

### ondragleave

`((this: GlobalEventHandlers, ev: DragEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/dragleave_event)

### ondragover

`((this: GlobalEventHandlers, ev: DragEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/dragover_event)

### ondragstart

`((this: GlobalEventHandlers, ev: DragEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/dragstart_event)

### ondrop

`((this: GlobalEventHandlers, ev: DragEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/drop_event)

### ondurationchange

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/durationchange_event)

### onemptied

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/emptied_event)

### onended

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/ended_event)

### onerror

`OnErrorEventHandler`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/error_event)

### onfocus

`((this: GlobalEventHandlers, ev: FocusEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/focus_event)

### onformdata

`((this: GlobalEventHandlers, ev: FormDataEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLFormElement/formdata_event)

### ongotpointercapture

`((this: GlobalEventHandlers, ev: PointerEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/gotpointercapture_event)

### oninput

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/input_event)

### oninvalid

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLInputElement/invalid_event)

### onkeydown

`((this: GlobalEventHandlers, ev: KeyboardEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/keydown_event)

### onkeypress

`((this: GlobalEventHandlers, ev: KeyboardEvent) => any) | null`

@deprecated

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/keypress_event)

### onkeyup

`((this: GlobalEventHandlers, ev: KeyboardEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/keyup_event)

### onload

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/load_event)

### onloadeddata

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/loadeddata_event)

### onloadedmetadata

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/loadedmetadata_event)

### onloadstart

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/loadstart_event)

### onlostpointercapture

`((this: GlobalEventHandlers, ev: PointerEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/lostpointercapture_event)

### onmousedown

`((this: GlobalEventHandlers, ev: MouseEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/mousedown_event)

### onmouseenter

`((this: GlobalEventHandlers, ev: MouseEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/mouseenter_event)

### onmouseleave

`((this: GlobalEventHandlers, ev: MouseEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/mouseleave_event)

### onmousemove

`((this: GlobalEventHandlers, ev: MouseEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/mousemove_event)

### onmouseout

`((this: GlobalEventHandlers, ev: MouseEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/mouseout_event)

### onmouseover

`((this: GlobalEventHandlers, ev: MouseEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/mouseover_event)

### onmouseup

`((this: GlobalEventHandlers, ev: MouseEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/mouseup_event)

### onpaste

`((this: GlobalEventHandlers, ev: ClipboardEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/paste_event)

### onpause

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/pause_event)

### onplay

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/play_event)

### onplaying

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/playing_event)

### onpointercancel

`((this: GlobalEventHandlers, ev: PointerEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointercancel_event)

### onpointerdown

`((this: GlobalEventHandlers, ev: PointerEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointerdown_event)

### onpointerenter

`((this: GlobalEventHandlers, ev: PointerEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointerenter_event)

### onpointerleave

`((this: GlobalEventHandlers, ev: PointerEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointerleave_event)

### onpointermove

`((this: GlobalEventHandlers, ev: PointerEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointermove_event)

### onpointerout

`((this: GlobalEventHandlers, ev: PointerEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointerout_event)

### onpointerover

`((this: GlobalEventHandlers, ev: PointerEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointerover_event)

### onpointerrawupdate

`((this: GlobalEventHandlers, ev: Event) => any) | null`

Available only in secure contexts.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointerrawupdate_event)

### onpointerup

`((this: GlobalEventHandlers, ev: PointerEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/pointerup_event)

### onprogress

`((this: GlobalEventHandlers, ev: ProgressEvent<EventTarget>) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/progress_event)

### onratechange

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/ratechange_event)

### onreset

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLFormElement/reset_event)

### onresize

`((this: GlobalEventHandlers, ev: UIEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLVideoElement/resize_event)

### onscroll

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/scroll_event)

### onscrollend

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/scrollend_event)

### onsecuritypolicyviolation

`((this: GlobalEventHandlers, ev: SecurityPolicyViolationEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/securitypolicyviolation_event)

### onseeked

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/seeked_event)

### onseeking

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/seeking_event)

### onselect

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLInputElement/select_event)

### onselectionchange

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/selectionchange_event)

### onselectstart

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Node/selectstart_event)

### onslotchange

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLSlotElement/slotchange_event)

### onstalled

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/stalled_event)

### onsubmit

`((this: GlobalEventHandlers, ev: SubmitEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLFormElement/submit_event)

### onsuspend

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/suspend_event)

### ontimeupdate

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/timeupdate_event)

### ontoggle

`((this: GlobalEventHandlers, ev: ToggleEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/toggle_event)

### ontouchcancel

`((this: GlobalEventHandlers, ev: TouchEvent) => any) | null | undefined`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/touchcancel_event)

### ontouchend

`((this: GlobalEventHandlers, ev: TouchEvent) => any) | null | undefined`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/touchend_event)

### ontouchmove

`((this: GlobalEventHandlers, ev: TouchEvent) => any) | null | undefined`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/touchmove_event)

### ontouchstart

`((this: GlobalEventHandlers, ev: TouchEvent) => any) | null | undefined`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/touchstart_event)

### ontransitioncancel

`((this: GlobalEventHandlers, ev: TransitionEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/transitioncancel_event)

### ontransitionend

`((this: GlobalEventHandlers, ev: TransitionEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/transitionend_event)

### ontransitionrun

`((this: GlobalEventHandlers, ev: TransitionEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/transitionrun_event)

### ontransitionstart

`((this: GlobalEventHandlers, ev: TransitionEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/transitionstart_event)

### onvolumechange

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/volumechange_event)

### onwaiting

`((this: GlobalEventHandlers, ev: Event) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLMediaElement/waiting_event)

### onwebkitanimationend

`((this: GlobalEventHandlers, ev: Event) => any) | null`

@deprecated

This is a legacy alias of `onanimationend`.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationend_event)

### onwebkitanimationiteration

`((this: GlobalEventHandlers, ev: Event) => any) | null`

@deprecated

This is a legacy alias of `onanimationiteration`.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationiteration_event)

### onwebkitanimationstart

`((this: GlobalEventHandlers, ev: Event) => any) | null`

@deprecated

This is a legacy alias of `onanimationstart`.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/animationstart_event)

### onwebkittransitionend

`((this: GlobalEventHandlers, ev: Event) => any) | null`

@deprecated

This is a legacy alias of `ontransitionend`.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/transitionend_event)

### onwheel

`((this: GlobalEventHandlers, ev: WheelEvent) => any) | null`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Element/wheel_event)

### autofocus

`boolean`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/autofocus)

### dataset

`DOMStringMap`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/dataset)

### nonce

`string | undefined`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/nonce)

### tabIndex

`number`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/tabIndex)

### blur

`void`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/blur)

@returns`void`

### focus

`void`

[MDN Reference](https://developer.mozilla.org/docs/Web/API/HTMLElement/focus)

@paramoptions`FocusOptions | undefined`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/elements/NgElement>
