class VotingModel:
    def __init__(self):
        """Initialize the VotingModel with vote data and voter records."""
        self.voters_file = "voters.txt"
        self.votes_file = "results.txt"
        self.load_votes()

    def load_votes(self):
        """Load existing votes from the results file."""
        try:
            with open(self.votes_file, "r") as file:
                data = file.readlines()
                self.votes = {"Jane": int(data[0].strip()), "John": int(data[1].strip())}
        except FileNotFoundError:
            self.votes = {"Jane": 0, "John": 0}

    def has_already_voted(self, voter_id):
        """
        Check if the voter ID exists in the voters.txt file.

        Args:
            voter_id (str): The unique ID of the voter.

        Returns:
            bool: True if the voter has already voted, False otherwise.
        """
        try:
            with open(self.voters_file, "r") as file:
                voters = file.readlines()
                return voter_id in [v.split()[0] for v in voters]
        except FileNotFoundError:
            return False

    def record_vote(self, voter_id, candidate):
        """
        Record the voter's ID and increment the vote count for the candidate.

        Args:
            voter_id (str): The unique ID of the voter.
            candidate (str): The candidate the voter selected.
        """
        self.modify_csv(voter_id, candidate)
        self.votes[candidate] += 1
        with open(self.votes_file, "w") as file:
            file.write(f"{self.votes['Jane']}\n{self.votes['John']}\n")

    def modify_csv(self, voter_id, candidate):
        """
        Modify voters.txt by updating an entry or appending new ones.

        Args:
            voter_id (str): The unique ID of the voter.
            candidate (str): The candidate the voter selected.
        """
        try:
            with open(self.voters_file, "r") as file:
                voters = file.readlines()

            updated = False
            with open(self.voters_file, "w") as file:
                for line in voters:
                    if line.startswith(voter_id):
                        file.write(f"{voter_id} {candidate}\n")
                        updated = True
                    else:
                        file.write(line)
                if not updated:
                    file.write(f"{voter_id} {candidate}\n")
        except FileNotFoundError:
            with open(self.voters_file, "w") as file:
                file.write(f"{voter_id} {candidate}\n")

    def clear_fields(self):
        """Clear the voter ID field and reset candidate selection."""
        self.ui.line_edit_id.clear()
        self.ui.radio_jane.setChecked(False)
        self.ui.radio_john.setChecked(False)




