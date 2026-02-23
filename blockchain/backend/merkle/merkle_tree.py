import hashlib


def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


class MerkleTree:

    def __init__(self, leaves):
        self.leaves = leaves
        self.levels = []
        if leaves:
            self.build_tree()

    def build_tree(self):
        current_level = self.leaves.copy()
        self.levels = [current_level]

        while len(current_level) > 1:
            next_level = []

            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i + 1] if i + 1 < len(current_level) else left
                combined = sha256(left + right)
                next_level.append(combined)

            current_level = next_level
            self.levels.append(current_level)

    def get_root(self):
        if not self.levels:
            return None
        return self.levels[-1][0]

    def get_proof(self, index):
        proof = []

        for level in self.levels[:-1]:
            pair_index = index ^ 1
            if pair_index < len(level):
                proof.append(level[pair_index])
            index = index // 2

        return proof

    @staticmethod
    def verify_proof(leaf, proof, root, index):
        computed = leaf

        for sibling in proof:
            if index % 2 == 0:
                computed = sha256(computed + sibling)
            else:
                computed = sha256(sibling + computed)
            index = index // 2

        return computed == root

    # 🔴 NEW: Remove leaf for revocation
    def remove_leaf(self, leaf_hash):
        if leaf_hash not in self.leaves:
            return False

        self.leaves.remove(leaf_hash)

        if self.leaves:
            self.build_tree()
        else:
            self.levels = []

        return True