package anagrams

import "testing"

func TestGetSignature(t *testing.T) {
	type args struct {
		word string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{"empty string", args{""}, ""},
		{"already sorted", args{"abcdefg"}, "ABCDEFG"},
		{"vinyl", args{"vinyl"}, "ILNVY"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := SignatureOf(tt.args.word); got != tt.want {
				t.Errorf("GetSignature() = %v, want %v", got, tt.want)
			}
		})
	}
}
