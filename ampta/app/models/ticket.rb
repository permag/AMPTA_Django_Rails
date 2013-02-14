class Ticket < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date, :status_id, :project_id
  belongs_to :user
  belongs_to :project
  belongs_to :status

  validates :name,
            :presence => true,
            :uniqueness => { :scope => :project_id, :case_sensitive => false, :message => "already exists in this project" },
            :length => { :in => 3..30, :allow_blank => true }

  validates_presence_of :description, :start_date, :end_date

  validate :validate_end_date_before_start_date,
           :validate_start_date_in_project_scope,
           :validate_end_date_in_project_scope


  def validate_end_date_before_start_date
    if end_date && start_date
      errors.add(:end_date, "must be greater than start date") if end_date <= start_date
    end
  end

  def validate_end_date_in_project_scope
    if end_date && start_date
      p = Project.find(project_id)
      errors.add(:end_date, "cannot be later than project end date - #{p.end_date.to_date.to_formatted_s(:long_ordinal)}") if end_date > p.end_date
    end
  end

  def validate_start_date_in_project_scope
    if end_date && start_date
      p = Project.find(project_id)
      errors.add(:start_date, "cannot be earlier than project start date - #{p.start_date.to_date.to_formatted_s(:long_ordinal)}") if start_date < p.start_date
    end
  end

end
