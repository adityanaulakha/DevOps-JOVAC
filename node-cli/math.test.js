const { add, sub } = require('../math');

test('add', () => {
    expect(add(2, 3)).toBe(5);
});

test('subtract', () => {
    expect(sub(2, 1)).toBe(1);
});
