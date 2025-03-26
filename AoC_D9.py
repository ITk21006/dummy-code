with open("E:\Code\input.txt") as f:
    ns = list(map(int, f.read().strip()))

# Part 1
disk = []  
for i, n in enumerate(ns):
    disk += [None if i % 2 else i // 2] * n # Add `n` elements to the disk, alt between `None` and `i // 2`

head = ns[0]  # Set initial position
while head < len(disk):
    if disk[head]:  # If `None`, move forward
        head += 1
    elif num := disk.pop():  # If `None`, pop last element from disk
        disk[head] = num  # Place popped element at the current position

print(sum(i * n for i, n in enumerate(disk)))

# Part 2
blocks = []  
head = 0  # Set initial position
for i, n in enumerate(ns):
    if not i % 2:  # Only process even numbers
        blocks.append((i // 2, head, head + n)) # Add block to the list (ID, start, end)
    head += n  # Move head forward by `n`

# Move blocks in reverse order of their IDs
for to_move in range(i // 2, -1, -1):
    # Find the block with the current ID to move
    block = next(b for b in blocks if b[0] == to_move)
    _, start, end = block
    space_needed = end - start  # Calculate the space needed for the block

    # Find a suitable position to move the block
    for i, ((_, _, end1), (_, start2, _)) in enumerate(zip(blocks, blocks[1:])):
        if end1 == end:  # If the block is already at the end, stop
            break
        if start2 - end1 >= space_needed:  # Check if there is enough space to move the block
            # Insert the block at the new position and remove it from the old position
            blocks.insert(i + 1, (to_move, end1, end1 + space_needed))
            blocks.remove(block)
            break

# Calculate sum of `block_id * index` for all blocks
print(
    sum(
        block_id * index
        for block_id, start, end in blocks
        for index in range(start, end)
    )
)