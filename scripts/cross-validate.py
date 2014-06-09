
m_list = [0, 1, 2]
p_list = [0, 1, 2]
t_list = [0, 2]

male_or_female = "female"

output_file = "../output/%s_cross_validation_3buckets_midis50_threshold50.out" % male_or_female
out = open(output_file, 'w')

for m in m_list:
	for p in p_list:
		for t in t_list:

			total_f1 = 0.0
			total_p = 0.0
			total_r = 0.0
			total_acc = 0.0

			for i in range(5):
				filename = "../output/%s_3buckets_midis50_threshold50/output_%d_%d_%d_%d.out" % (male_or_female, i, m, p, t)

				f = open(filename)
				lines = f.readlines()

				prec = float(lines[5].strip().split(' ')[1])
				rec = float(lines[6].strip().split(' ')[1])
				f1 = float(lines[7].strip().split(' ')[1])
				acc = float(lines[8].strip().split(' ')[1])

				f.close()

				total_p += prec
				total_r += rec
				total_f1 += f1
				total_acc += acc

			out.write("META: %d, PROSODIC: %d, TEXTUAL: %d" % (m, p, t) + "\n")
			out.write("---> precision: %f, recall: %f, f1: %f, accuracy: %f" % (total_p / 5.0, total_r / 5.0, total_f1 / 5.0, total_acc / 5.0) + "\n\n")

out.close()


