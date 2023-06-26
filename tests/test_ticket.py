def test_save_ticket(tmp_path, sample_ticket): 
    path = tmp_path / 'ticket.txt'
    sample_ticket.save_ticket(path)
    assert path.read_text() == str(sample_ticket) 
