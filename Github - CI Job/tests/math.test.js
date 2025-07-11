const { add, sub } = require('../math');

test('add 2 + 3 should be 5', () => {
  expect(add(2, 3)).toBe(5);
});

test('subtract 2 - 1 should be 1', () => {
  expect(sub(2, 1)).toBe(1);
});
